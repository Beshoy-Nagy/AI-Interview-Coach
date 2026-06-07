import re


def extract_score(text):

    match = re.search(
        r"Score:\s*(\d+)",
        text
    )

    if match:

        return int(match.group(1))

    return None