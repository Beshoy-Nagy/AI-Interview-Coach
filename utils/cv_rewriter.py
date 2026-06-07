from utils.ollama_client import ask_llm


def rewrite_cv(
    cv_text,
    job_description
):

    prompt = f"""
You are an expert AI resume writer and technical recruiter.

Your task is to improve the CV so it better matches the job description.

CV:
{cv_text}

JOB DESCRIPTION:
{job_description}

Rules:
- Do NOT invent experience.
- Do NOT invent technologies.
- Do NOT invent projects.
- Do NOT invent certifications.
- Do NOT invent achievements.
- Do NOT invent metrics or percentages.
- Do NOT add skills that are not present in the CV.
- Only rewrite and improve existing content.
- Reorganize sections if needed.
- Improve wording and professionalism.
- Highlight experiences that are most relevant to the job description.
- Use ATS-friendly formatting and keywords ONLY when they already exist in the CV.
- If important skills from the job description are missing, do NOT add them to the CV.

Return exactly the following sections:

Professional Summary

Improved Skills Section

Improved Project Descriptions

ATS Optimization Suggestions

In ATS Optimization Suggestions:
- List skills that are requested in the job description but missing from the CV.
- Explain how the candidate can gain or demonstrate those skills.
- Do NOT pretend the candidate already has them.

Return the rewritten CV content only.
"""

    return ask_llm(prompt)