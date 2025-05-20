import streamlit as st
import requests
import json

# Your OpenRouter API key
API_KEY = "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"

st.title("👽 Chat with Meta")
st.write("Using the `Meta: Llama 3.3 8B Instruct (free)`  via OpenRouter API")

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
        "model": "deepseek/deepseek-r1:free",
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
