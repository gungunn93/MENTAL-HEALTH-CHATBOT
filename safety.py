CRISIS_KEYWORDS = [
    "suicide", "kill myself", "end my life", "self-harm",
    "don't want to live", "want to die", "hurt myself",
    "no reason to live", "can't go on"
]

CRISIS_RESPONSE = """
I hear you, and I'm genuinely concerned about you right now. 
Please reach out to someone who can help immediately:

🆘 iCall (India): 9152987821
🆘 Vandrevala Foundation: 1860-2662-345 (24/7, free)
🆘 AASRA: 9820466627
🆘 International: findahelpline.com

You matter. Please don't go through this alone. 💙
"""

def is_crisis(text: str) -> bool:
    text_lower = text.lower()
    return any(keyword in text_lower for keyword in CRISIS_KEYWORDS)