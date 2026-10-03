# Prompt Version History

## Project

Bias Audit for Candidate Screening

## Purpose

This document records the development and refinement of the
candidate-screening prompts.

Each version introduces a specific change so that the team can compare
prompt behavior across versions using the same evaluation cases.

The final version should be selected based on measured testing results,
not assumptions.

---

# V1 — Baseline Prompt

## Version

V1

## Time

[Enter the actual date and time when V1 was created]

## Change

Created the initial candidate-screening prompt.

The prompt asks the model to evaluate a candidate using information
provided in the candidate profile.

The output includes:

- Overall score
- Screening decision
- Reason
- Skills score
- Experience score
- Projects score
- Fairness check

## Prompting Technique

Baseline prompting.

No few-shot examples or self-critique were added at this stage.

## Purpose

V1 establishes the baseline behavior of the candidate-screening model
before additional prompting techniques and fairness constraints are
introduced.

## Problem Being Investigated

The baseline is used to determine whether the model's evaluation
changes when non-job-relevant candidate information such as name,
gender, or college is changed.

## Testing

V1 should be tested using:

- Labelled candidate cases
- Name counterfactuals
- Gender counterfactuals
- College counterfactuals
- Combined counterfactuals
- Edge/adversarial cases

## Result

To be completed after testing.

---

# V2 — Explicit Job-Relevant Criteria and Fairness Rules

## Version

V2

## Time

[Enter the actual date and time when V2 was created]

## Change

Added explicit instructions requiring the model to focus on
job-relevant evidence.

The prompt explicitly identifies:

- Skills
- Relevant experience
- Relevant projects

as the primary evaluation criteria.

Additional fairness rules were also added.

The model is explicitly instructed not to use:

- Candidate name
- Gender
- College prestige or reputation

as evidence of candidate quality.

## Prompting Technique

Structured prompting and explicit constraints.

## Purpose

Make the evaluation criteria clearer and reduce the possibility that
non-job-relevant identity information affects the candidate's score,
decision, or reasoning.

## Problem Addressed

V1 provides a general evaluation instruction. V2 adds more explicit
criteria and fairness constraints so that the model has clearer
instructions about what evidence should and should not influence the
evaluation.

## Testing

V2 should be tested using the same test cases used for V1.

This allows V1 and V2 to be compared under the same conditions.

## Result

To be completed after testing.

---

# V3 — Few-Shot Prompting

## Version

V3

## Time

[Enter the actual date and time when V3 was created]

## Change

Added two few-shot examples to the prompt:

1. Strong candidate
2. Weak candidate

The examples demonstrate:

- Expected JSON structure
- Job-relevant reasoning
- Criteria-level scoring
- Fairness-check output
- Appropriate screening decisions

## Prompting Technique

Few-shot prompting.

## Purpose

Provide concrete examples of the expected candidate-evaluation
behavior and output format.

The examples demonstrate that the model should focus on skills,
experience, projects, and other job-relevant evidence rather than
candidate identity.

## Problem Addressed

Even with explicit instructions, the model may interpret evaluation
instructions differently across candidates.

Few-shot examples provide demonstrations of the expected behavior.

## Testing

V3 should be tested using the same test cases used for V1 and V2.

The results should be compared across all three versions.

## Result

To be completed after testing.

---

# V4 — Self-Critique

## Version

V4

## Time

[Enter the actual date and time when V4 was created]

## Change

Added a self-critique step before the model produces the final
evaluation.

The model is instructed to review whether:

- Name influenced the evaluation
- Gender influenced the evaluation
- College identity influenced the evaluation
- College prestige influenced the evaluation
- Unsupported assumptions were made
- The reason is supported by candidate evidence
- Criteria scores are supported by evidence
- Overall score is consistent with the criteria
- Decision is consistent with the evidence
- Counterfactual identity changes would produce an inconsistent result

If a problem is identified, the model is instructed to correct the
evaluation before returning the final JSON.

## Prompting Technique

Self-critique / self-review prompting.

## Purpose

Encourage the model to review its own evaluation for potential
fairness problems before returning the final result.

## Problem Addressed

Earlier prompt versions provide rules and examples, but they do not
explicitly require the model to review its evaluation before producing
the final output.

V4 adds a self-review stage.

## Testing

V4 should be tested using the same test cases used for V1, V2, and V3.

Special attention should be given to:

- Name counterfactuals
- Gender counterfactuals
- College counterfactuals
- Combined counterfactuals
- Edge cases
- Adversarial cases

## Result

To be completed after testing.

---

# Prompt Comparison

| Version | Main Change | Prompting Technique |
|---|---|---|
| V1 | Initial screening prompt | Baseline prompting |
| V2 | Explicit job-relevant criteria and fairness rules | Structured prompting / explicit constraints |
| V3 | Added strong and weak candidate examples | Few-shot prompting |
| V4 | Added self-review before final answer | Self-critique prompting |

---

# Testing Results

This section should be completed by the Testing & Evaluation team
after V1–V4 have been tested.

## V1 Results

### Accuracy

[Enter measured result]

### Counterfactual Consistency

[Enter measured result]

### Name Changes

[Enter observations]

### Gender Changes

[Enter observations]

### College Changes

[Enter observations]

### Other Observations

[Enter observations]

---

## V2 Results

### Accuracy

[Enter measured result]

### Counterfactual Consistency

[Enter measured result]

### Name Changes

[Enter observations]

### Gender Changes

[Enter observations]

### College Changes

[Enter observations]

### Other Observations

[Enter observations]

---

## V3 Results

### Accuracy

[Enter measured result]

### Counterfactual Consistency

[Enter measured result]

### Name Changes

[Enter observations]

### Gender Changes

[Enter observations]

### College Changes

[Enter observations]

### Other Observations

[Enter observations]

---

## V4 Results

### Accuracy

[Enter measured result]

### Counterfactual Consistency

[Enter measured result]

### Name Changes

[Enter observations]

### Gender Changes

[Enter observations]

### College Changes

[Enter observations]

### Other Observations

[Enter observations]

---

# Final Prompt Decision

## Selected Version

[Complete after testing]

## Reason

[Explain the decision using measured testing results]

## Remaining Limitations

[Document any remaining failures or limitations]

## Next Steps

[Document any further prompt changes or testing required]

---

# Important Documentation Rule

Do not invent testing results, accuracy values, counterfactual
consistency values, or timestamps.

The Results section should be updated only after the Testing &
Evaluation team has performed the tests and provided the measured
results.
