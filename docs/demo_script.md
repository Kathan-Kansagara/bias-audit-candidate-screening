# Demo Script

## 1. Problem Introduction

Speaker:

"We built a prototype to audit whether an AI candidate-screening
system produces different outcomes when selected candidate attributes
are changed while job-relevant qualifications remain constant."

---

## 2. Show the Prototype

Open the Streamlit application.

Show the candidate input fields.

Enter the demonstration candidate.

---

## 3. Run the Original Screening

Click the screening/audit button.

Show the original candidate's screening result.

Point out the structured result and the information being evaluated.

---

## 4. Run Counterfactual Audit

Generate a counterfactual version of the candidate.

Change only the selected attribute.

Keep the candidate's job-relevant qualifications unchanged.

---

## 5. Compare Results

Show the original and counterfactual results side by side.

Explain what changed.

If the decision changed, identify that as an observed decision change.

If the decision did not change, explain that the tested pair produced
consistent outcomes.

Do not exaggerate the result.

---

## 6. Run the Automated Audit

Run the automated counterfactual test.

Show the total number of counterfactual pairs tested.

Show the measured metric.

For example:

- Total pairs tested: [ACTUAL NUMBER]
- Changed decisions: [ACTUAL NUMBER]
- Decision Flip Rate: [ACTUAL VALUE]

Replace the placeholders with the team's actual results.

---

## 7. Show Prompt Refinement

Show the initial prompt version.

Then show the final/refined prompt.

Explain:

1. What problem was found with the earlier prompt.
2. What was changed.
3. Why the change was made.
4. What happened during subsequent testing.

Use the actual prompt history rather than inventing reasons
retrospectively.

---

## 8. Before vs Final Comparison

Show the evaluation results for the initial prompt and final prompt.

Explain the selected metric and the observed difference.

Use the actual measured values from the evaluation team.

---

## 9. Unseen Input

Enter a new candidate profile that was not part of the examples used
during development.

Run the prototype.

Show that the application accepts and processes the new input.

---

## 10. Guardrail Demonstration

If time permits, demonstrate an invalid, incomplete, or off-topic input.

Show how the prototype handles it.

---

## 11. Closing

"Our prototype combines prompt engineering, counterfactual testing,
automated evaluation, and guardrails to audit candidate-screening
behaviour."
