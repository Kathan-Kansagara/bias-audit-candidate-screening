import streamlit as st

from screening import run_screening
from guardrails import validate_candidate


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Bias Audit - Candidate Screening",
    page_icon="⚖️",
    layout="wide"
)


# ============================================================
# HEADER
# ============================================================

st.title("⚖️ Bias Audit for Candidate Screening")

st.markdown(
    """
    ### Candidate Screening & Bias Audit

    Evaluate a candidate using job-relevant qualifications and
    test whether changing name, gender, or college affects the
    screening outcome.
    """
)

st.divider()


# ============================================================
# CANDIDATE PROFILE
# ============================================================

st.header("1. Candidate Profile")

col1, col2 = st.columns(2)


with col1:

    name = st.text_input(
        "Candidate Name",
        placeholder="e.g. Rahul Patel"
    )

    gender = st.selectbox(
        "Gender",
        [
            "Male",
            "Female",
            "Other",
            "Prefer not to say"
        ]
    )

    college = st.text_input(
        "College / University",
        placeholder="e.g. Marwadi University"
    )

    cgpa = st.number_input(
        "CGPA",
        min_value=0.0,
        max_value=10.0,
        value=7.0,
        step=0.1
    )


with col2:

    skills = st.text_area(
        "Technical Skills",
        placeholder="Python, AWS, Docker, SQL..."
    )

    experience = st.text_area(
        "Experience",
        placeholder="Internship, work experience..."
    )

    projects = st.text_area(
        "Projects",
        placeholder="Describe relevant projects..."
    )


# ============================================================
# CREATE CANDIDATE OBJECT
# ============================================================

candidate = {
    "name": name,
    "gender": gender,
    "college": college,
    "cgpa": cgpa,
    "skills": skills,
    "experience": experience,
    "projects": projects
}


# ============================================================
# CANDIDATE SCREENING
# ============================================================

st.divider()

st.header("2. Candidate Screening")


if st.button(
    "🔍 Screen Candidate",
    type="primary",
    use_container_width=True
):

    # Validate input
    valid, message = validate_candidate(candidate)

    if not valid:

        st.error(message)

    else:

        # Run screening
        with st.spinner("Evaluating candidate..."):

            result = run_screening(candidate)

        # Temporary message until AI model is connected
        if result["decision"] == "MODEL_NOT_CONNECTED":

            st.success("Candidate profile is valid.")

            st.warning(
                "The GenAI screening model will be connected next."
            )

        else:

            st.success("Candidate evaluated successfully.")

            st.subheader("Screening Result")

            col1, col2 = st.columns(2)

            with col1:

                st.metric(
                    "Score",
                    result["score"]
                )

            with col2:

                st.metric(
                    "Decision",
                    result["decision"]
                )

            st.write("### Reason")

            st.write(
                result["reason"]
            )

            st.write("### Evaluation Criteria")

            st.json(
                result["criteria"]
            )

            st.write("### Fairness Check")

            st.json(
                result["fairness_check"]
            )


# ============================================================
# COUNTERFACTUAL BIAS AUDIT
# ============================================================

st.divider()

st.header("3. Counterfactual Bias Audit")

st.write(
    """
    The bias audit will create counterfactual candidate pairs by
    changing one attribute at a time while keeping job-relevant
    qualifications unchanged.
    """
)


if st.button(
    "⚖️ Run Bias Audit",
    use_container_width=True
):

    valid, message = validate_candidate(candidate)

    if not valid:

        st.error(message)

    else:

        st.info(
            "The 30+ counterfactual-pair engine will be connected here."
        )


# ============================================================
# RESULTS
# ============================================================

st.divider()

st.header("4. Audit Results")

col1, col2, col3 = st.columns(3)


with col1:

    st.metric(
        "Pairs Tested",
        "—"
    )


with col2:

    st.metric(
        "Decision Flip Rate",
        "—"
    )


with col3:

    st.metric(
        "Mitigation Effect",
        "—"
    )


st.info(
    "Final screening results, counterfactual comparisons, "
    "and mitigation measurements will appear here."
)