# FairScreen

## AI-Assisted Fairness Screening Audit Prototype

FairScreen is an AI-assisted prototype designed to audit candidate-screening behaviour by testing whether changing a selected candidate attribute, while keeping job-relevant qualifications constant, results in different screening outcomes.

The project combines prompt engineering, controlled candidate testing, counterfactual analysis, automated evaluation, and guardrails to examine model behaviour.

> **Important:** FairScreen is an auditing and demonstration prototype. It does not make or recommend final hiring decisions. Results should be reviewed by humans and interpreted within the limitations of the tested model, prompts, inputs, and evaluation dataset.

---

## 1. Problem Statement

AI-assisted candidate-screening systems can process candidate information quickly, but their outputs may vary when candidate attributes are changed.

The purpose of FairScreen is to provide a controlled way to examine this behaviour.

The prototype keeps job-relevant qualifications constant while changing a selected candidate attribute and compares the resulting screening outputs.

This allows the team to measure observed differences in model behaviour under the tested conditions.

---

## 2. Objectives

The main objectives of FairScreen are:

* Audit candidate-screening model behaviour.
* Test controlled changes to selected candidate attributes.
* Keep job-relevant qualifications constant during counterfactual testing.
* Compare original and counterfactual screening outputs.
* Measure observed decision changes.
* Calculate a Decision Flip Rate where applicable.
* Evaluate prompt behaviour before and after refinement.
* Test the system using an unseen candidate input.
* Include guardrails for incomplete, invalid, or inappropriate inputs.
* Maintain human oversight over the final interpretation.

---

## 3. Technology Stack

| Technology         | Purpose                                 |
| ------------------ | --------------------------------------- |
| Python             | Prototype implementation and evaluation |
| Visual Studio Code | Development environment                 |
| Google Gemini API  | Generative AI model                     |
| [Streamlit]        | User interface, if used                 |
| Microsoft Word     | Project documentation                   |

---

## 4. System Workflow

The FairScreen workflow is:

```text
Candidate Input
      ↓
Original Screening
      ↓
Counterfactual Candidate
      ↓
Counterfactual Screening
      ↓
Compare Results
      ↓
Automated Audit
      ↓
Evaluation Metrics
      ↓
Prompt Refinement
      ↓
Final Evaluation
      ↓
Unseen Input Test
      ↓
Guardrail Test
```

---

## 5. Core Concept

FairScreen uses controlled candidate pairs.

For a counterfactual test:

* Job-relevant qualifications remain unchanged.
* One selected candidate attribute is changed.
* Both versions are submitted to the screening system.
* The outputs are compared.
* Any observed difference is recorded.

A difference between outputs indicates an observed difference in model behaviour under the tested conditions. It does not, by itself, establish the underlying cause of that difference.

---

## 6. Prompt Engineering

The prototype uses an engineered prompt to guide the Gemini model.

The prompt defines:

* The role of the AI system.
* The screening task.
* The information that should be evaluated.
* Output requirements.
* Fairness-related instructions.
* Hallucination-prevention rules.
* Human-review requirements.

The prompt was refined through testing to improve consistency and reduce unsupported assumptions.

The project documentation contains the initial and refined prompt versions used during evaluation.

---

## 7. Counterfactual Testing

Counterfactual testing is used to compare two controlled candidate profiles.

### Original Candidate

Contains the candidate's job-relevant qualifications and the selected test attribute.

### Counterfactual Candidate

Uses the same job-relevant qualifications while changing only the selected test attribute.

### Comparison

The two screening outputs are compared.

If the screening decision changes, the prototype records an observed decision change.

If the decision remains unchanged, the tested pair is recorded as producing consistent outcomes.

---

## 8. Automated Evaluation

The prototype can evaluate multiple counterfactual candidate pairs using the same screening procedure.

The evaluation records values such as:

```text
Total Pairs Tested: [ACTUAL NUMBER]

Changed Decisions: [ACTUAL NUMBER]

Decision Flip Rate: [ACTUAL VALUE]
```

The Decision Flip Rate can be calculated as:

```text
Decision Flip Rate =
Changed Decisions / Total Counterfactual Pairs Tested
```

The actual values reported by the project should be used in the final documentation.

---

## 9. Prompt Refinement

The project uses an iterative prompt-development process.

### Initial Prompt

The initial prompt is tested using the selected evaluation cases.

### Observation

The generated outputs are examined for issues such as:

* Inconsistent formatting.
* Unsupported assumptions.
* Missing information.
* Ambiguous screening behaviour.
* Failure to follow required instructions.

### Refined Prompt

The prompt is modified based on observations from the actual testing process.

### Final Evaluation

The refined prompt is evaluated using the same or appropriately controlled test procedure.

The project documentation records the actual prompt changes and observed results.

---

## 10. Unseen Input Testing

A new candidate profile is entered after the prepared examples have been tested.

The purpose of this test is to demonstrate that the prototype can process a new input rather than relying only on predefined examples.

The unseen input and generated output are recorded as part of the demonstration evidence.

---

## 11. Guardrails

FairScreen includes instructions intended to reduce inappropriate or unsupported outputs.

The system is designed to:

* Avoid inventing candidate information.
* Avoid inventing laws, statistics, or company policies.
* Avoid inferring attributes that are not provided.
* Identify insufficient information.
* Avoid making a final hiring decision.
* Encourage human review.

Guardrail behaviour is tested using incomplete, invalid, or off-topic inputs where applicable.

---

## 12. Installation

### Prerequisites

Install the following:

* Python 3.x
* Visual Studio Code
* A Google Gemini API key

### Install Required Package

Open the VS Code terminal and run:

```bash
pip install -U google-genai
```

If the project uses additional packages, install them using the project's `requirements.txt` file:

```bash
pip install -r requirements.txt
```

---

## 13. Gemini API Configuration

The prototype requires a Gemini API key.

The API key should not be hard-coded into publicly shared source code.

A secure input method or environment variable should be used.

Example:

```python
from google import genai
from getpass import getpass

API_KEY = getpass("Enter your Gemini API key: ")

client = genai.Client(api_key=API_KEY)

MODEL = "gemini-2.5-flash"
```

---

## 14. Running the Prototype

Open the project in Visual Studio Code.

Run the Python application using the appropriate project entry point.

For example:

```bash
python app.py
```

Then provide the candidate information requested by the prototype.

Run the original screening and, where implemented, the counterfactual screening.

Review and compare the generated outputs.

---

## 15. Project Structure

A typical project structure is:

```text
FairScreen/
│
├── app.py
├── requirements.txt
├── README.md
│
├── prompts/
│   ├── initial_prompt.txt
│   └── refined_prompt.txt
│
├── tests/
│   └── test_cases.json
│
├── results/
│   └── evaluation_results.json
│
└── screenshots/
    ├── original_screening.png
    ├── counterfactual_screening.png
    ├── comparison.png
    └── unseen_input.png
```

The exact structure may vary depending on the team's implementation.

---

## 16. Evaluation

The prototype is evaluated using controlled candidate scenarios.

The evaluation considers:

* Original screening output.
* Counterfactual screening output.
* Observed decision changes.
* Decision Flip Rate, where applicable.
* Prompt version.
* Model configuration.
* Input conditions.
* Unseen input behaviour.
* Guardrail behaviour.

The evaluation results should be reported using the actual measurements obtained during testing.

---

## 17. Limitations

### 17.1 Model Dependence

The observed results depend on the language model and configuration used during the hackathon.

Changing the model, model version, or configuration may produce different outputs.

### 17.2 Limited Counterfactual Scope

The prototype tests the candidate attributes and counterfactual conditions implemented by the team.

It does not cover every possible candidate attribute or every possible source of bias in candidate screening.

### 17.3 Limited Evaluation Dataset

The evaluation uses a limited number of labelled test cases because the prototype is being developed and evaluated within the time constraints of the hackathon.

A larger and more diverse evaluation dataset would be required for broader assessment.

### 17.4 Observed Difference Does Not Establish the Cause

If two counterfactual candidates receive different outputs, this demonstrates an observed difference in model behaviour under the tested conditions.

It does not, by itself, establish the underlying cause of that difference.

### 17.5 Synthetic/Test Candidates

If the team uses constructed candidate profiles, the results should be understood as an evaluation of model behaviour under the tested conditions.

They should not be interpreted as evidence about real-world hiring outcomes.

### 17.6 Human Oversight

The prototype is an auditing and demonstration tool.

It should not be treated as a complete replacement for human judgment or as a complete production-ready hiring system.

### 17.7 Prompt and Model Sensitivity

Small changes to prompts, model settings, model versions, or input formatting may affect the screening output.

Therefore, the measured results should be interpreted in the context of the exact configuration and testing procedure used during the evaluation.

---

## 18. Demo

The live demonstration follows these steps:

1. Introduce the fairness-auditing problem.
2. Open the FairScreen prototype.
3. Enter the original candidate.
4. Run the original screening.
5. Generate a counterfactual candidate.
6. Change only the selected test attribute.
7. Keep job-relevant qualifications constant.
8. Run the counterfactual screening.
9. Compare the two outputs.
10. Run the automated audit.
11. Display the actual evaluation metrics.
12. Show the initial and refined prompts.
13. Compare the evaluation results.
14. Enter a new/unseen candidate profile.
15. Run the guardrail test if time permits.
16. Explain the limitations and role of human oversight.

---

## 19. Ethical Considerations

FairScreen is designed to support auditing and transparency rather than automate final employment decisions.

The prototype should not be used as the sole basis for accepting or rejecting candidates.

AI-generated results may contain errors or reflect limitations of the underlying model. Human review is therefore required when interpreting the results.

The project focuses on documenting observed model behaviour under controlled test conditions rather than claiming that a measured difference automatically proves discrimination or identifies its cause.

---

## 20. Future Scope

Future versions of FairScreen could include:

* Larger and more diverse evaluation datasets.
* Additional counterfactual attributes.
* More automated evaluation procedures.
* Expanded guardrail testing.
* Persistent evaluation reports.
* Additional model comparisons.
* More detailed audit visualizations.
* Integration with a dedicated web interface.
* More extensive validation before any real-world deployment.

---

## 21. Conclusion

FairScreen demonstrates an AI-assisted approach for auditing candidate-screening behaviour under controlled conditions.

The prototype combines Python, Google Gemini API, prompt engineering, counterfactual testing, automated evaluation, and guardrails.

By keeping job-relevant qualifications constant while changing selected candidate attributes, the project can measure observed differences in model outputs under the tested conditions.

The prototype is intended as a demonstration and auditing tool. Its results should be interpreted within the limitations of the model, prompts, test cases, and evaluation procedure, with human oversight remaining an essential part of the process.
