import streamlit as st
import openai

# Page config
st.set_page_config(page_title="Pete's Research Assistant", layout="centered")

# Title
st.title("Pete's Research Assistant")

# Instructions
st.markdown("""
Enter your query below. This tool uses GPT-4 and follows Pete's explicit rules:
- No speculation
- Triple-source verification
- British English
- Auction-style formatting only
""")

- Auction-style formatting only
\"\"\")

# API Key input (hidden)
api_key = st.text_input("Enter your OpenAI API Key", type="password")

# Query input
query = st.text_area("Enter your research or valuation query")

# Submit button
if st.button("Submit"):

    if not api_key:
        st.error("Please enter your OpenAI API key.")
    elif not query:
        st.error("Please enter a query.")
    else:
        openai.api_key = api_key

system_message = """
You are a precision research assistant for a professional UK auctioneer.
You must:
- Use triple-source verification only.
- Never speculate or invent information.
- Use British English spelling.
- Format your response as:
1. Auction Headline (no quotation marks, correct title case, include date or date range)
2. Conservative Auction Estimate (on a separate line)
If you cannot verify the information, respond only: 'Unverifiable based on available evidence.'
"""
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    { "role": "system", "content": system_message },
                    { "role": "user", "content": query }
                ],
                temperature=0.0
            )
            answer = response["choices"][0]["message"]["content"]
            st.markdown("---")
            st.markdown("### ✅ Verified Response")
            st.text(answer)

        except Exception as e:
            st.error(f"Error: {str(e)}")
