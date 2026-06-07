from utils.ollama_client import ask_llm


def analyze_interview(
    evaluations
):

    prompt = f"""
Analyze the following interview evaluations.

{evaluations}

Return:

Strengths

Weaknesses

Top 3 Skills To Improve

Final Recommendation
"""

    return ask_llm(
        prompt
    )