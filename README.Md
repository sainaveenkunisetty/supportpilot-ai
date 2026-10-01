# SupportPilot AI — Customer Support Resolution Agent

## Overview

SupportPilot AI is a Python-based customer support assistant that uses a locally running language model to answer support questions using an approved knowledge base. It includes basic safety checks, insufficient-evidence handling, and escalation records for issues that require human review.

## Features

- **Local LLM integration:** Uses Ollama with the `llama3.2:1b` model.
- **Knowledge retrieval:** Uses TF-IDF and cosine similarity to find relevant support documentation.
- **Safety checks:** Detects selected sensitive inputs and unsafe requests.
- **Human escalation:** Creates reference IDs for cases requiring human review.
- **Insufficient-evidence handling:** Avoids generating answers when no sufficiently relevant documentation is retrieved.
- **Streamlit interface:** Provides a simple chat-based user interface.
- **Automated evaluation:** Tests expected behavior across support scenarios.

## Technology Stack

- Python
- Streamlit
- Ollama
- Llama 3.2 (1B)
- scikit-learn
- TF-IDF and cosine similarity
- pytest

## Project Structure

```text
supportpilot-ai/
├── agent/
│   ├── assistant.py
│   ├── escalation.py
│   ├── knowledge_base.py
│   ├── safe_logging.py
│   └── safety.py
├── data/
│   └── support_knowledge.txt
├── tests/
├── app.py
├── evaluate.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Setup and Installation

1. Install Python and Ollama.
2. Download the local model:

   ```bash
   ollama pull llama3.2:1b
   ```

3. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   ```

   Windows PowerShell:

   ```powershell
   .venv\Scripts\Activate.ps1
   ```

4. Install project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Start the application:

   ```bash
   python -m streamlit run app.py
   ```

6. Run automated evaluation:

   ```bash
   python evaluate.py
   ```

7. Run unit tests:

   ```bash
   python -m pytest -v
   ```

## Safety and Limitations

This is a demonstration project. Safety rules are basic pattern-based checks and are not comprehensive. Escalation records are generated locally and are not automatically sent to a real support team. Answers depend on the quality and coverage of the supplied documentation.

Do not use real passwords, verification codes, payment details, or private customer data when testing.

## Future Improvements

- Improve grounding and answer validation.
- Add a persistent database for escalation records.
- Integrate with a ticketing system.
- Add role-based access control and stronger privacy protections.
- Expand the evaluation dataset and measure answer quality.
- Support additional approved knowledge sources.

## Author

Developed as a learning project demonstrating retrieval-based question answering, local LLM integration, safety checks, escalation handling, and automated testing.