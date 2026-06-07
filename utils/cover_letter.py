from utils.ollama_client import ask_llm


def generate_cover_letter(
    cv_text,
    job_description
):

    prompt = f"""
You are an expert technical recruiter.

Write a professional cover letter based ONLY on the candidate's actual CV.

Candidate CV:
{cv_text}

Job Description:
{job_description}

Rules:
- Do NOT invent skills.
- Do NOT invent experience.
- Do NOT invent technologies.
- Do NOT invent certifications.
- Do NOT invent projects.
- Do NOT claim knowledge of tools that are missing from the CV.
- Use only information found in the CV.
- Highlight skills that match the job description.
- If some job requirements are missing, do not mention them as existing skills.
- Keep the tone professional and realistic.
- Tailor the cover letter to the job description.
- Mention why the candidate is interested in the role.
- Mention the strongest matching projects from the CV.
- Do not use placeholders such as [Company Name] or [Date].
- Return only the cover letter.

At the end add a short section:

Areas I Am Currently Expanding

Include 3-5 skills that are requested in the job description but missing from the CV and present them as areas the candidate is actively learning or planning to strengthen.

Do NOT claim mastery of those skills.
"""

    return ask_llm(prompt)