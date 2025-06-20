from langchain_experimental.agents import create_csv_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
import streamlit as st

# Set page config FIRST
st.set_page_config(
    page_title="Ask your CSV",
    page_icon="📊",
    layout="wide",  # optional: use 'centered' or 'wide'
    initial_sidebar_state="expanded"
)

def main():
    load_dotenv()

    # Sidebar content
    with st.sidebar:
        st.title("🔗 About")
        st.markdown("""
        **Developer**: [Sahil Chalke](https://github.com/sahilchalke0001)

        **GitHub Repo**:  
        [github.com/sahilchalke0001/csv](https://github.com/sahilchalke0001/csv)

        **Powered by**:  
        - LangChain  
        - Google Gemini API  
        - Streamlit

        ---

        ⚙️ **Theme Toggle**  
        You can switch themes via the ⚙️ (settings) icon in the top-right corner.
        """)

    # Load API key
    if os.getenv("GOOGLE_API_KEY") is None or os.getenv("GOOGLE_API_KEY") == "":
        st.error("GOOGLE_API_KEY is not set")
        st.stop()

    st.title("Ask your CSV 📈")

    # Benefits Section
    st.markdown("""
    ### Why Use This Tool?
    - **Secure and Private**: Your data stays within your session and is never uploaded to external servers.
    - **No Coding Required**: Get insights from your CSV without writing a single line of code.
    - **Natural Language Interface**: Ask questions in plain English like "What’s the total revenue in 2023?"
    - **Fast Analysis**: Instantly process large CSVs.
    - **Privacy-Focused**: CSV files are processed only during your session and are not stored or shared. No third-party access.
    - **Powered by Gemini + LangChain**: Reliable, intelligent results.

    ---
    """)


    # FAQ or Sample Questions
    with st.expander("📌 Sample Questions / FAQ (AFTER UPLOADING THE REQUIRED CSV)"):
        st.markdown("""
        - What is the average salary?
        - How many entries are from 2023?
        - List all rows where profit is greater than 10,000.
        - What’s the maximum value in column X?
        - Which category has the highest total?

        You can ask anything the AI can interpret from the CSV.
        """)

    # Upload and interact
    csv_file = st.file_uploader("Upload your CSV file", type="csv")

    if csv_file is not None:
        # Load the LLM
        llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-flash",
            temperature=0,
            verbose=True
        )

        # Create CSV Agent
        agent = create_csv_agent(
            llm,
            csv_file,
            verbose=True,
            allow_dangerous_code=True
        )

        # User input
        user_question = st.text_input("Ask a question about your CSV:")

        if user_question:
            with st.spinner("Thinking..."):
                st.write(agent.run(user_question))


if __name__ == "__main__":
    main()
