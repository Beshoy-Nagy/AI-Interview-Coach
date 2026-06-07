from utils.ollama_client import ask_llm

def match_cv_to_job(
    cv_text,
    job_description
):

    prompt = f"""
You are a professional technical recruiter.

Compare the following CV with the Job Description.

CV:
{cv_text}

Job Description:
{job_description}

Return:

Match Score: X%

Strong Matches:
- ...

Missing Skills:
- ...

Recommended Improvements:
- ...

Final Recommendation:
...
"""

    return ask_llm(prompt)