from utils.ollama_client import ask_llm

def generate_learning_roadmap(
    report,
    assessment
):

    prompt = f"""
You are an AI career mentor.

Based on the interview report and assessment:

REPORT:
{report}

ASSESSMENT:
{assessment}

Create a learning roadmap.

Return:

Current Level

Top Skills To Improve

30-Day Learning Plan

Week 1:
...

Week 2:
...

Week 3:
...

Week 4:
...

Recommended Resources

Final Advice
"""

    return ask_llm(prompt)