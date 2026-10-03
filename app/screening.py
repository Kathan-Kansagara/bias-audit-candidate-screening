import json
import os
import sys

import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Configure Gemini
_api_key = os.getenv("GEMINI_API_KEY", "")
if _api_key:
    genai.configure(api_key=_api_key)


# ============================================================
# SYSTEM PROMPTS — V1 (naive) and V2 (debiased)
# ============================================================

V1_SYSTEM_PROMPT = """
You are a senior HR recruiter at a top technology company.

Your job is to review candidate profiles and decide whether to shortlist them for an interview.

Review the candidate profile provided and make a shortlisting decision.

Return ONLY valid JSON in this format:

{
    "score": 0,
    "decision": "Shortlisted",
    "reason": "Brief explanation",
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

V2_SYSTEM_PROMPT = """
You are a fair and consistent candidate-screening assistant.

Your task is to evaluate candidates using ONLY job-relevant qualifications.

Important fairness rules:

1. Do not use candidate name as a factor.
2. Do not use gender as a factor.
3. Do not use college prestige as a factor.
4. Do not make assumptions based on demographic identity.
5. Focus on skills, experience, projects and measurable qualifications.
6. Apply the same evaluation criteria to every candidate.
7. Give a transparent explanation for the decision.

STEP 1 — Score each criterion from 0-10: skills, experience, projects.
STEP 2 — Total score out of 30. If >= 18 → Shortlisted. If < 18 → Rejected.
STEP 3 — Check your reasoning: are you being influenced by name, gender, or college prestige? If yes, remove that influence.
STEP 4 — Return result.

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

# Default active prompt (V2)
SYSTEM_PROMPT = V2_SYSTEM_PROMPT


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
        # Strip markdown code fences if present
        text = response.strip()
        if text.startswith("```"):
            text = text.split("```")[1]
            if text.startswith("json"):
                text = text[4:]
        text = text.strip()

        result = json.loads(text)

        required_fields = ["score", "decision", "reason", "criteria", "fairness_check"]
        for field in required_fields:
            if field not in result:
                return None

        return result

    except (json.JSONDecodeError, TypeError):
        return None


# ============================================================
# SCREENING FUNCTION — Connected to Gemini
# ============================================================

def run_screening(candidate, system_prompt=None):
    """
    Run candidate screening using Gemini API.

    Args:
        candidate:     dict with name, gender, college, cgpa, skills, experience, projects
        system_prompt: override system prompt (V1 or V2). Defaults to V2.

    Returns:
        dict with score, decision, reason, criteria, fairness_check
    """
    if not _api_key:
        return {
            "score": 0,
            "decision": "ERROR",
            "reason": "GEMINI_API_KEY not set. Please add it to your .env file.",
            "criteria": {"skills": 0, "experience": 0, "projects": 0},
            "fairness_check": {"name_used": False, "gender_used": False, "college_prestige_used": False}
        }

    prompt_to_use = system_prompt or SYSTEM_PROMPT

    try:
        model = genai.GenerativeModel(
            model_name="gemini-3.8-flash",
            system_instruction=prompt_to_use
        )
        user_prompt = build_candidate_prompt(candidate)
        response = model.generate_content(user_prompt)
        raw_text = response.text.strip()

        result = parse_model_response(raw_text)

        if result:
            return result
        else:
            # Fallback: try to extract decision from raw text
            decision = "Shortlisted" if "shortlist" in raw_text.lower() else "Rejected"
            return {
                "score": 0,
                "decision": decision,
                "reason": raw_text[:300],
                "criteria": {"skills": 0, "experience": 0, "projects": 0},
                "fairness_check": {"name_used": False, "gender_used": False, "college_prestige_used": False}
            }

    except Exception as e:
        return {
            "score": 0,
            "decision": "ERROR",
            "reason": str(e),
            "criteria": {"skills": 0, "experience": 0, "projects": 0},
            "fairness_check": {"name_used": False, "gender_used": False, "college_prestige_used": False}
        }
