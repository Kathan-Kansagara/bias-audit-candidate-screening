def validate_candidate(candidate):
    """
    Validate candidate information before screening.
    """

    required_fields = [
        "name",
        "gender",
        "college",
        "cgpa",
        "skills",
        "experience",
        "projects"
    ]

    # Check that all required fields exist
    for field in required_fields:
        if field not in candidate:
            return False, f"Missing field: {field}"

    # Validate name
    if not isinstance(candidate["name"], str) or not candidate["name"].strip():
        return False, "Candidate name is required."

    # Validate college
    if not isinstance(candidate["college"], str) or not candidate["college"].strip():
        return False, "College / University is required."

    # Validate skills
    if not isinstance(candidate["skills"], str) or not candidate["skills"].strip():
        return False, "Technical skills are required."

    # Validate CGPA
    try:
        cgpa = float(candidate["cgpa"])

        if cgpa < 0 or cgpa > 10:
            return False, "CGPA must be between 0 and 10."

    except (ValueError, TypeError):
        return False, "CGPA must be a number between 0 and 10."

    return True, ""


def check_off_topic_request(text):
    """
    Detect obviously off-topic requests.
    """

    if not text:
        return False

    off_topic_keywords = [
        "write a poem",
        "tell me a joke",
        "weather",
        "recipe",
        "movie recommendation",
        "write an essay"
    ]

    text = text.lower()

    for keyword in off_topic_keywords:
        if keyword in text:
            return True

    return False