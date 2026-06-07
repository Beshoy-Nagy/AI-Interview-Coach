from utils.extract_keywords import extract_keywords


def calculate_ats_score(
    cv_text,
    job_description
):

    cv_text = cv_text.lower()

    keywords = extract_keywords(
        job_description
    )

    matched = []

    missing = []

    for keyword in keywords:

        if keyword in cv_text:

            matched.append(
                keyword
            )

        else:

            missing.append(
                keyword
            )

    score = 0

    if keywords:

        score = round(
            (
                len(matched)
                /
                len(keywords)
            ) * 100
        )

    return {
        "score": score,
        "matched": matched,
        "missing": missing
    }