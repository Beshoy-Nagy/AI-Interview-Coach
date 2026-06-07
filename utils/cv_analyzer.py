from utils.ollama_client import ask_llm


def analyze_cv(cv_text):

    prompt = f"""
You are a senior technical recruiter.

Analyze this CV and return:

1. Candidate Name
2. Current Role
3. Technical Skills
4. Work Experience Summary
5. Projects
6. Strengths
7. Recommended Interview Topics

CV:

{cv_text}
"""

    return ask_llm(prompt)