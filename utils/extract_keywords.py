from utils.ollama_client import ask_llm


def extract_keywords(
    job_description
):

    prompt = f"""
Extract only the important technical skills from this job description.

Rules:
- Return only skills.
- One skill per line.
- No explanations.
- No numbering.
- Focus on technical skills, tools, frameworks, cloud services, programming languages, and AI concepts.

Job Description:

{job_description}
"""

    response = ask_llm(
        prompt
    )

    keywords = [
        line.strip().lower()
        for line in response.split("\n")
        if line.strip()
    ]

    return list(
        set(keywords)
    )