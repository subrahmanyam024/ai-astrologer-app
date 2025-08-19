import streamlit as st
from datetime import datetime, date

# Predefined zodiac signs and descriptions
zodiac_signs = {
    (3, 21): "Aries - Bold and ambitious, you're a natural leader! Today's energy favors taking initiative in new projects.",
    (4, 20): "Taurus - Reliable and patient, you value stability. Today, focus on grounding yourself and enjoying small comforts.",
    (5, 21): "Gemini - Versatile and witty, you love variety. Expect lively conversations and new ideas today!",
    (6, 21): "Cancer - Intuitive and sympathetic, you're family-oriented. Nurture your loved ones and trust your instincts today.",
    (7, 23): "Leo - Creative and generous, you shine in the spotlight. Your charisma opens doors today—seize the moment!",
    (8, 23): "Virgo - Practical and analytical, you're detail-oriented. Organize your tasks today for a productive outcome.",
    (9, 23): "Libra - Diplomatic and gracious, you seek harmony. Balance in relationships will bring peace today.",
    (10, 23): "Scorpio - Resourceful and brave, you're a passionate soul. Dive deep into your goals today for success.",
    (11, 22): "Sagittarius - Optimistic and freedom-loving, you're an adventurer. Explore new horizons today, even if just in thought.",
    (12, 22): "Capricorn - Disciplined and responsible, you're a goal-setter. Steady progress will lead to achievements today.",
    (1, 20): "Aquarius - Progressive and original, you're a humanitarian. Innovative ideas will spark inspiration today.",
    (2, 19): "Pisces - Compassionate and artistic, you're a dreamer. Let your creativity flow freely today."
}

def get_zodiac_sign(birth_date):
    month = birth_date.month
    day = birth_date.day
    for (m, d), desc in zodiac_signs.items():
        if (month == m and day >= d) or (month == m + 1 and day < d):
            return desc.split(" - ")[0], desc  # Return sign and full description
    if month == 12 and day >= 22 or month == 1 and day <= 19:
        return "Capricorn", zodiac_signs[(12, 22)]
    return "Unknown", "Unknown - Unable to determine zodiac sign. Please check your date of birth."

# Rule-based response for free-text question
def get_free_response(question, zodiac):
    question = question.lower()
    if "love" in question or "relationship" in question:
        return f"The stars align for {zodiac} in love today. Open your heart to new connections or deepen existing bonds with honesty."
    elif "career" in question or "job" in question:
        return f"For {zodiac}, career opportunities shine bright. Take bold steps toward your goals with confidence."
    elif "health" in question:
        return f"{zodiac}, the cosmos advises balance. Prioritize rest and mindfulness to boost your well-being."
    elif "school" in question or "education" in question or "hands dirty" in question:
        return f"{zodiac}, your learning journey sparkles today. Embrace hands-on experiences to grow and shine."
    elif "life" in question or "future" in question:
        return f"{zodiac}, the stars see a bright future. Pursue your dreams with passion, and the universe will guide your path."
    else:
        return f"{zodiac}, the universe encourages you to trust your intuition today. Reflect on your question for deeper insights."

# Streamlit UI
st.title("AI Astrologer App")

# Collect User Input
name = st.text_input("Enter your Name:")
dob = st.date_input("Enter your Date of Birth:", min_value=date(1900, 1, 1), max_value=date(2025, 12, 31), value=date(1990, 1, 1))
time = st.time_input("Enter your Time of Birth:")
place = st.text_input("Enter your Place of Birth:")

if st.button("Generate Horoscope"):
    if name and dob and time and place:
        zodiac, horoscope = get_zodiac_sign(dob)
        if zodiac == "Unknown":
            st.error(horoscope)
        else:
            st.success(f"Hello, {name}! Your zodiac sign is {zodiac}. {horoscope} Based on your birth details (DOB: {dob}, Time: {time}, Place: {place}), today's outlook is positive!")
    else:
        st.error("Please fill all fields.")

# Free-Text Question
st.subheader("Ask an Astrology Question")
question = st.text_input("Enter your astrology-related question:")
if st.button("Get Answer"):
    if question:
        zodiac, _ = get_zodiac_sign(dob) if dob else ("Unknown", "")
        if zodiac == "Unknown":
            st.error("Please generate horoscope first to determine your zodiac sign.")
        else:
            answer = get_free_response(question, zodiac)
            st.info(answer)
    else:
        st.error("Please enter a question.")