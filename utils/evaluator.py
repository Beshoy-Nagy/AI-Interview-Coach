from utils.ollama_client import ask_llm


def evaluate_answer(question, answer):

    prompt = f"""
You are a professional technical interviewer.

Question:
{question}

Candidate Answer:
{answer}

Evaluation Rules:

- Evaluate only the answer provided.
- Do not assume missing information is incorrect.
- Do not invent mistakes.
- Give credit for partially correct answers.
- Focus on the quality of the answer relative to the question.
- If the answer is technically correct but lacks detail, reduce the score moderately.
- Do not penalize the candidate for not mentioning advanced techniques.
- Do not penalize the candidate for role mismatch.
- If the question itself belongs to a different field, evaluate the answer based on that field.
- Reward practical experience, clear reasoning, and accurate technical explanations.
- Penalize only factual inaccuracies, contradictions, or poor explanations.
- Keep feedback constructive and realistic.

Scoring Guide:

9-10:
Excellent answer, technically correct, clear, and well explained.

7-8:
Good answer with minor missing details.

5-6:
Partially correct answer with noticeable gaps.

3-4:
Major gaps or misunderstandings.

0-2:
Incorrect answer or does not address the question.

Return exactly in this format:

Score: X/10

Strengths:
- ...
- ...

Weaknesses:
- ...
- ...

Suggested Improvement:
...
"""

    return ask_llm(prompt)