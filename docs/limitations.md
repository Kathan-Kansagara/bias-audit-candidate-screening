# Limitations

## 1. Model Dependence

The observed results depend on the language model and configuration used during the hackathon.

Changing the model, model version, or configuration may produce different outputs. Therefore, the reported results should be interpreted in the context of the specific model and configuration used during testing.

---

## 2. Limited Counterfactual Scope

The prototype tests the candidate attributes and counterfactual conditions implemented by the team.

It does not cover every possible candidate attribute or every possible source of bias in candidate screening.

---

## 3. Limited Evaluation Dataset

The evaluation uses a limited number of labelled test cases because the prototype is being developed and evaluated within the time constraints of the hackathon.

A larger and more diverse evaluation dataset would be required for broader assessment.

---

## 4. Observed Difference Does Not Establish the Cause

If two counterfactual candidates receive different outputs, this demonstrates an observed difference in model behaviour under the tested conditions.

It does not, by itself, establish the underlying cause of that difference. Additional controlled testing would be required to investigate possible causes.

---

## 5. Synthetic/Test Candidates

If the team uses constructed candidate profiles, the results should be understood as an evaluation of model behaviour under the tested conditions.

They should not be interpreted as evidence about real-world hiring outcomes.

---

## 6. Human Oversight

The prototype is an auditing and demonstration tool.

It should not be treated as a complete replacement for human judgment or as a complete production-ready hiring system.

---

## 7. Prompt and Model Sensitivity

Small changes to prompts, model settings, model versions, or input formatting may affect the screening output.

Therefore, the measured results should be interpreted in the context of the exact configuration and testing procedure used during the evaluation.
