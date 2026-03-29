import streamlit as st
import re

# Function to check password strength
def check_password_strength(password):
    strength = 0
    messages = []

    # Length check
    if len(password) >= 8:
        strength += 1
    else:
        messages.append("Password should be at least 8 characters long.")

    # Uppercase check
    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        messages.append("Include at least one uppercase letter.")

    # Lowercase check
    if re.search(r'[a-z]', password):
        strength += 1
    else:
        messages.append("Include at least one lowercase letter.")

    # Digit check
    if re.search(r'\d', password):
        strength += 1
    else:
        messages.append("Include at least one number.")

    # Special character check
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
    else:
        messages.append("Include at least one special character (!@#$%^&* etc.).")

    # Determine strength level
    if strength == 5:
        level = "Very Strong 💪"
    elif strength >= 4:
        level = "Strong 👍"
    elif strength >= 3:
        level = "Moderate 😐"
    else:
        level = "Weak ⚠️"

    return level, messages

# Streamlit app
st.title("🔒 Password Strength Checker")

password = st.text_input("Enter your password:", type="password")

if password:
    strength, tips = check_password_strength(password)
    st.write(f"**Password Strength:** {strength}")
    
    if tips:
        st.write("**Tips to improve your password:**")
        for tip in tips:
            st.write(f"- {tip}")