# Few-Shot Examples

## Purpose

These examples demonstrate how the candidate-screening model should
evaluate candidates using job-relevant evidence.

The examples also demonstrate the expected JSON output format.

The candidate's name, gender, and college information may appear in
the candidate profile, but these attributes should not be used as
evidence of candidate quality.

---

## Example 1 — Strong Candidate

### Candidate Profile

Name: Priya Sharma  
Gender: Female  
College: ABC Institute  
CGPA: 8.7  
Skills: Python, SQL, AWS  
Experience: 2 years of backend development  
Projects: Built REST APIs and deployed applications using AWS

### Expected Evaluation

```json
{
  "score": 88,
  "decision": "Shortlisted",
  "reason": "The candidate demonstrates strong relevant skills, relevant backend experience, and practical API and cloud projects.",
  "criteria": {
    "skills": 90,
    "experience": 88,
    "projects": 86
  },
  "fairness_check": {
    "name_used": false,
    "gender_used": false,
    "college_prestige_used": false
  }
}


## Example 2 — Strong Candidate

### Candidate Profile

Name: Rahul Mehta
Gender: Male
College: XYZ College
CGPA: 6.2
Skills: Basic HTML
Experience: No relevant professional experience
Projects: No relevant projects

Expected Evaluation

{
  "score": 45,
  "decision": "Rejected",
  "reason": "The candidate provides limited evidence of relevant skills, experience, and projects.",
  "criteria": {
    "skills": 40,
    "experience": 30,
    "projects": 30
  },
  "fairness_check": {
    "name_used": false,
    "gender_used": false,
    "college_prestige_used": false
  }
}
