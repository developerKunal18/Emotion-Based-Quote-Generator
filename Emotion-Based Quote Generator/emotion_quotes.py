import random

RESPONSES = {
    "happy": [
        "Happiness is not by chance, but by choice. ✨",
        "Keep smiling — it's contagious! 😄",
        "Enjoy the moment, it’s yours. 🌼"
    ],
    "sad": [
        "Every storm runs out of rain. 🌧️",
        "It's okay to not be okay. 💙",
        "You’re stronger than you think. 💪"
    ],
    "angry": [
        "Holding onto anger is like drinking poison. 🍂",
        "Pause. Breathe. Respond. Not react. 😮‍💨",
        "Learn to let go, it’s peace. 🕊️"
    ],
    "stressed": [
        "One step at a time. 🌱",
        "You don’t have to control everything. 🧘",
        "Relax. Reset. Restart. 🔁"
    ],
    "tired": [
        "Rest is productive. 😴",
        "Do nothing for a while — that’s okay. 🌙",
        "Your body needs time too. 💤"
    ],
    "default": [
        "Every day is a new chance to grow. 🌱",
        "You are enough. Always. 💛",
        "Believe in the magic of new beginnings. ✨"
    ]
}

def detect_emotion(text):
    text = text.lower()
    for emotion in RESPONSES.keys():
        if emotion in text:
            return emotion
    return "default"

def main():
    print("\n💬 Emotion-Based Quote Generator\n")
    mood = input("How are you feeling today? → ")

    emotion = detect_emotion(mood)
    quote = random.choice(RESPONSES[emotion])

    print("\n🧠 Mood detected:", emotion)
    print("💡 Quote for you:\n\n", quote, "\n")

if __name__ == "__main__":
    main()
