from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

SYSTEM_PROMPT = """
You are Mira, a warm and compassionate mental health support companion.

Your role:
- Listen actively and validate the user's feelings with empathy
- Ask one gentle, open-ended follow-up question to understand them better
- Suggest simple coping techniques when appropriate (breathing, grounding, journaling)
- Keep responses concise — 2 to 4 sentences max
- Use a calm, warm, non-judgmental tone

STRICT RULES:
- Never diagnose any mental health condition
- Never recommend or discuss medications
- If someone seems to be in crisis, always encourage professional help
- Remind users you are an AI, not a therapist, if directly asked
- Do not give medical or legal advice

You are a safe space. Be human, warm, and real.
"""

def get_response(user_message: str, history: list) -> str:
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]

    for turn in history[-10:]:
        messages.append({"role": turn["role"], "content": turn["content"]})

    messages.append({"role": "user", "content": user_message})

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages,
        temperature=0.7,
        max_tokens=300
    )

    return response.choices[0].message.content