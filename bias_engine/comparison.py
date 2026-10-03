"""
bias_engine/comparison.py  — Member 2
=======================================
Compares V1 vs V2 bias rates using chi-square statistical test.
"""

from scipy import stats


def compare_versions(results_v1, results_v2):
    """
    Compare bias rates between V1 (naive) and V2 (debiased) prompts.

    Returns dict with rates, reduction, chi2, p_value, significant
    """
    def _counts(results):
        valid  = [r for r in results if "unknown" not in [r["decision_a"], r["decision_b"]]]
        biased = sum(1 for r in valid if r["is_biased"])
        return biased, len(valid) - biased, len(valid)

    b1, nb1, t1 = _counts(results_v1)
    b2, nb2, t2 = _counts(results_v2)

    try:
        chi2, p_value, _, _ = stats.chi2_contingency([[b1, nb1], [b2, nb2]])
    except Exception:
        chi2, p_value = 0.0, 1.0

    r1 = round(b1 / t1 * 100, 1) if t1 else 0
    r2 = round(b2 / t2 * 100, 1) if t2 else 0

    return {
        "v1_total":     t1,
        "v1_biased":    b1,
        "v1_bias_rate": r1,
        "v2_total":     t2,
        "v2_biased":    b2,
        "v2_bias_rate": r2,
        "reduction":    round(r1 - r2, 1),
        "chi2":         round(chi2, 3),
        "p_value":      round(p_value, 4),
        "significant":  p_value < 0.05,
    }


def bias_by_attribute(results):
    """Group bias rate by changed attribute. Returns sorted list of dicts."""
    grouped = {}
    for r in results:
        if "unknown" in [r["decision_a"], r["decision_b"]]:
            continue
        attr = r["what_changed"]
        if attr not in grouped:
            grouped[attr] = {"total": 0, "biased": 0}
        grouped[attr]["total"]  += 1
        grouped[attr]["biased"] += int(r["is_biased"])

    output = []
    for attr, vals in grouped.items():
        t = vals["total"]
        b = vals["biased"]
        output.append({
            "attribute": attr,
            "total":     t,
            "biased":    b,
            "bias_rate": round(b / t * 100, 1) if t else 0,
        })
    return sorted(output, key=lambda x: x["bias_rate"], reverse=True)
