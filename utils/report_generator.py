from utils.ollama_client import ask_llm


def generate_report(evaluations):

    prompt = f"""
You are a senior technical interviewer.

Based on these interview evaluations:

{evaluations}

Create a final interview report.

Return:

Overall Performance

Strengths

Weaknesses

Recommended Topics To Study

Final Recommendation
(Hire / Consider / Needs Improvement)

Be concise and professional.
"""

    return ask_llm(prompt)