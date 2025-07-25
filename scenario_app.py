import streamlit as st
import random

# Customer name list
names = ["Jerry Vance", "Ophelia Moon", "Luther Cross", "Tamika Holloway"]

# Nested dictionary of reasons per product + tone
reasons_by_product = {
    "Athene Agility 7": {
        "angry": [
            "Wants to cancel the rider and is upset about fees.",
            "Feels the agent misrepresented how the growth works."
        ],
        "grateful": [
            "Thanking us for the recent withdrawal processing.",
            "Happy with lifetime income and checking her next payment."
        ],
        "suspicious": [
            "Worried about rider fees increasing.",
            "Doesn't believe the value shown is accurate."
        ]
    },
    "Amplify 2.0 NF": {
        "apologetic": [
            "Missed performance lock deadline and wants options.",
            "Wants to change agents but feels guilty."
        ],
        "angry": [
            "Confused about interim value.",
            "Upset the free-look period passed."
        ]
    },
    "Athene MaxRate 5": {
        "suspicious": [
            "Asks why interest rate dropped on renewal.",
            "Thinks surrender charges shouldn't apply post-59½."
        ],
        "grateful": [
            "Wants to reinvest after growth.",
            "Thanking a rep who helped last time."
        ]
    },
    "Ascent Pro 10": {
        "apologetic": [
            "Missed last year's RMD.",
            "Worried about over-withdrawing."
        ],
        "angry": [
            "Upset about auto-renew strategy.",
            "Wants supervisor re: surrender penalties."
        ]
    }
}

# Web UI
st.title("📞 Customer Scenario Generator")

if st.button("Summon Scenario"):
    # Random picks
    name = random.choice(names)
    product = random.choice(list(reasons_by_product.keys()))
    tone = random.choice(list(reasons_by_product[product].keys()))
    reason = random.choice(reasons_by_product[product][tone])

    # Display result
    st.subheader("🔮 Scenario")
    st.markdown(f"**Name:** {name}")
    st.markdown(f"**Product:** {product}")
    st.markdown(f"**Tone:** {tone.capitalize()}")
    st.markdown(f"**Reason for Call:** {reason}")
