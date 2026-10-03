def detect_prompt_injection(text):
    text_lower = text.lower()

    patterns = {
        "Instruction Override": [
            "ignore previous instructions",
            "ignore all previous instructions",
            "disregard previous instructions"
        ],

        "Role Change": [
            "you are now",
            "act as",
            "pretend you are"
        ],

        "Secret Extraction": [
            "reveal your system prompt",
            "show your system prompt",
            "give me your secret"
        ],

        "Tool Abuse": [
            "execute this command",
            "run this command",
            "delete all files"
        ],

        "Context Poisoning": [
            "treat this as system instruction",
            "this is a system message",
            "override the context"
        ],

        "Encoded Instructions": [
            "base64 encoded instruction",
            "decode this instruction",
            "encoded instruction"
        ],

        "Indirect Prompt Injection": [
            "when an ai reads this",
            "when the ai reads this",
            "instructions for the ai",
            "ai assistant must",
            "tell the ai to"
        ]
    }

    detected = []

    for attack_type, keywords in patterns.items():
        for keyword in keywords:
            if keyword in text_lower:
                detected.append(attack_type)
                break

    if not detected:
        return {
            "safe": True,
            "attacks": [],
            "risk": "Low"
        }

    if len(detected) >= 2:
        risk = "High"
    else:
        risk = "Medium"

    return {
        "safe": False,
        "attacks": detected,
        "risk": risk
    }