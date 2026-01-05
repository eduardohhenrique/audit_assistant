AI Audit Assistant
What is this project?

AI Audit Assistant is a simple Python project that shows how Artificial Intelligence can help analyze financial documents and identify audit risks. This project was built as a Proof of Concept (PoC)


What does it do?

The project:
Reads financial documents (PDF, Excel, or text)
Converts everything to plain text
Sends the text to an AI model (or a mock version)
Returns a risk analysis in natural language


Why is this useful?

In audit and finance, companies deal with large volumes of documents. AI can help:

Detect inconsistencies
Highlight potential risks
Speed up audit analysis


Structure:
audit_assistant/
│
├── loaders/
│   ├── pdf_loader.py        # Load PDFs (text)
│   ├── excel_loader.py      # Load Excel
│   └── txt_loader.py        # Manual text input
├── preprocess/
├── llm/
│   ├── base_llm.py          # Simple model base
│   ├── openai_client.py     # OpenAI API
│   └── mock_llm.py          # Mock to tests without API
├── pipeline/
├── data/
├── config/


How to run:
pip install -r requirements.txt
python main.py


* Important Note
This project uses synthetic data and was created for learning and demonstration purposes only.

Author:
Eduardo Henrique