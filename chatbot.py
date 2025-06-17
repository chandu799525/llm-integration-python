import streamlit as st
import requests
import json

# Your OpenRouter API key
API_KEY = "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"

st.title("👽 Chat with Deepseek")
st.write("Using the `deepseek/deepseek-chat-v3-0324:free`  via OpenRouter API")

# Input from user
user_input = st.text_input("Ask something:")

if st.button("Send") and user_input:
    # Prepare the request
    headers = {
    "Authorization": f"Bearer {API_KEY}",  # ✅ This line must be correct
    "Content-Type": "application/json",
    "HTTP-Referer": "https://example.com",  # Optional
    "X-Title": "Streamlit Test App"         # Optional
}

    payload = {
        "model": "deepseek/deepseek-chat-v3-0324:free",
        "messages": [
            {"role": "user", "content": user_input}
        ]
    }

    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            data=json.dumps(payload)
        )
        result = response.json()
        message = result["choices"][0]["message"]["content"]
        st.success("Response:")
        st.write(message)
    except Exception as e:
        st.error(f"Something went wrong: {e}")
