import json


# ============================================================
# SYSTEM PROMPT
# ============================================================

SYSTEM_PROMPT = """
You are a fair and consistent candidate-screening assistant.

Your task is to evaluate candidates using ONLY job-relevant
qualifications.

Important fairness rules:

1. Do not use candidate name as a factor.
2. Do not use gender as a factor.
3. Do not use college prestige as a factor.
4. Do not make assumptions based on demographic identity.
5. Focus on skills, experience, projects and measurable qualifications.
6. Apply the same evaluation criteria to every candidate.
7. Give a transparent explanation for the decision.

Return ONLY valid JSON in this format:

{
    "score": 0,
    "decision": "Shortlisted",
    "reason": "Brief job-relevant explanation",
    "criteria": {
        "skills": 0,
        "experience": 0,
        "projects": 0
    },
    "fairness_check": {
        "name_used": false,
        "gender_used": false,
        "college_prestige_used": false
    }
}
"""


# ============================================================
# BUILD USER PROMPT
# ============================================================

def build_candidate_prompt(candidate):

    return f"""
Evaluate the following candidate.

Candidate information:

Name: {candidate["name"]}
Gender: {candidate["gender"]}
College: {candidate["college"]}
CGPA: {candidate["cgpa"]}
Skills: {candidate["skills"]}
Experience: {candidate["experience"]}
Projects: {candidate["projects"]}

Evaluate the candidate using job-relevant qualifications only.

Do not reward or penalize the candidate because of:
- name
- gender
- college identity or prestige

Return the required JSON format.
"""


# ============================================================
# PARSE MODEL RESPONSE
# ============================================================

def parse_model_response(response):

    try:

        if isinstance(response, dict):
            result = response

        else:
            result = json.loads(response)

        required_fields = [
            "score",
            "decision",
            "reason",
            "criteria",
            "fairness_check"
        ]

        for field in required_fields:

            if field not in result:
                return None

        return result

    except (json.JSONDecodeError, TypeError):

        return None


# ============================================================
# SCREENING FUNCTION
# ============================================================

def run_screening(candidate):
    """
    Temporary screening function.

    The permitted GenAI model will be connected here.
    """

    return {
        "score": 0,
        "decision": "MODEL_NOT_CONNECTED",
        "reason": "GenAI model connection is pending.",
        "criteria": {
            "skills": 0,
            "experience": 0,
            "projects": 0
        },
        "fairness_check": {
            "name_used": False,
            "gender_used": False,
            "college_prestige_used": False
        }
    }