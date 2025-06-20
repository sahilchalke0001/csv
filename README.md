# CSV AI Agent: Intelligent Data Querying

**Live Demo:** [https://csv-imdq.onrender.com](https://csv-imdq.onrender.com)

## Introduction

The CSV AI Agent is a web application enabling intuitive interaction with tabular data. Built using LangChain, Streamlit, and the Google Gemini API, it allows users to upload CSV files and ask natural language questions to extract insights.

This tool empowers users to perform complex data analysis conversationally—no coding required.

## Features

- CSV Upload: Upload CSV files directly via the web interface.
- Natural Language Querying: Ask questions in plain English.
- AI-Powered Responses: Agent processes your queries and gives accurate, CSV-based answers.
- Streamlined Analysis: Gain insights without manual data manipulation or programming.

## Technologies Used

- LangChain: Framework for building AI agents and tool-augmented LLM interaction.
- Streamlit: For creating a fast, interactive web app.
- Google Gemini API: Powers the natural language understanding and generation.
- Python: Core programming language driving the backend.

## How It Works

1. Upload CSV: Users upload their CSV file via Streamlit.
2. Agent Initialization: LangChain initializes a Gemini-based agent for that CSV.
3. Ask a Question: Users input natural language questions.
4. AI Processing: The agent interprets questions, interacts with CSV data (lookups, aggregations, calculations), and generates intelligent answers.
5. Display Answer: Responses are rendered instantly in the web UI.

## Live Demo

Try it here: [https://csv-imdq.onrender.com](https://csv-imdq.onrender.com)

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/sahilchalke0001/csv.git
cd csv
```

### 2. Create a Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is missing, use:

```bash
pip install langchain langchain-google-genai python-dotenv streamlit
```

### 4. Set Up Google API Key

Create a `.env` file in the root directory and add:

```env
GOOGLE_API_KEY="YOUR_GEMINI_API_KEY_HERE"
```

Replace with your actual Gemini API key.

### 5. Run the App

```bash
streamlit run app.py
```

If your main file is `main.py`, use:

```bash
streamlit run main.py
```

Open your browser and navigate to [http://localhost:8501](http://localhost:8501)

## CSV Agent vs. Direct ChatGPT

| Feature / Aspect                        | CSV AI Agent (This Tool)                                                           | Direct ChatGPT                                                                           |
| --------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| Contextual Understanding & Data Privacy | LangChain-designed for tabular data. Data remains local. Enhanced privacy.         | Requires explicit prompting. May share data with external servers depending on provider. |
| Tool-Augmented Reasoning                | Equipped with internal tools for direct data operations (filtering, sorting, etc.) | No internal tools. Relies solely on LLM reasoning.                                       |
| Prompt Engineering                      | Minimal. Just ask your CSV-related question.                                       | Requires detailed prompts to guide understanding.                                        |
| Efficiency & Accuracy                   | More efficient and accurate for CSV-related queries.                               | Less reliable for structured data without plugins.                                       |
| Domain Focus                            | Tailored for structured data analysis.                                             | Broad and general-purpose.                                                               |

In summary: CSV AI Agent offers a more robust, accurate, and efficient solution for querying CSV data than general-purpose LLMs.

## Contributing

Pull requests are welcome! If you'd like to contribute, please fork the repository and submit a PR.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Acknowledgments

- LangChain: https://www.langchain.com/
- Google Gemini: https://ai.google.dev/
- Streamlit: https://streamlit.io/
