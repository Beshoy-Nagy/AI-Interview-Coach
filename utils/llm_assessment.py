from utils.ollama_client import ask_llm


def llm_assessment(results):

    prompt = f"""
You are a Senior Technical Hiring Manager.

Based on the following interview session:

{results}

Evaluate the candidate and provide:

1. Candidate Level
(Beginner / Junior / Mid-Level / Senior)

2. Technical Confidence Score (0-100)

3. Communication Score (0-100)

4. Problem Solving Score (0-100)

5. Strengths

6. Weaknesses

7. Hiring Decision
(Strong Hire / Hire / Consider / Reject)

8. Short Explanation

Be concise and professional.
"""

    return ask_llm(prompt)