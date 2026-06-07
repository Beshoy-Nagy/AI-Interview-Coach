from utils.ollama_client import ask_llm


def generate_questions(
    cv_text,
    job_description
):

    prompt = f"""
Generate exactly 10 interview questions.

Use:
1. The candidate CV.
2. The job description.

Rules:
- Focus on skills that appear in both the CV and job description.
- Include technical questions.
- Include project-based questions.
- Include behavioral questions.
- Return only questions.
- One question per line.
- No headings.
- No explanations.

CV:
{cv_text}

JOB DESCRIPTION:
{job_description}
"""

    return ask_llm(prompt)