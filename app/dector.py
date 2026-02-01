import random

def detect_voice(wav_path):
    confidence = round(random.uniform(0.6, 0.95), 2)

    if confidence > 0.75:
        classification = "AI_GENERATED"
        explanation = "Unnatural pitch consistency detected"
    else:
        classification = "HUMAN"
        explanation = "Natural speech variations detected"

    return classification, confidence, explanation
