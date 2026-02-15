# AI Data Analyst Agent 🕵️‍♂️📊

A professional, autonomous Data Analyst Agent built with **FastAPI**, **Groq LLM (Llama 3)**, and **Google ADK** concepts. This agent automates the data analysis process, providing structured insights, visualizations, and business recommendations from your CSV datasets.

## 🚀 Features

-   **Automated Data Analysis**: Upload any CSV/Excel file and get an instant, comprehensive analysis.
-   **Structured 6-Step Workflow**: follows a strict rigorous analytical process:
    1.  Data Understanding
    2.  Descriptive Statistics
    3.  Insight Generation
    4.  Visualization Suggestions
    5.  ML Recommendations
    6.  Business Strategy
-   **High-Performance Backend**: Built on **FastAPI** for asynchronous, high-speed API responses.
-   **Lightning Fast Inference**: Powered by **Groq** and **Llama 3** for near-instant analysis generation.
-   **Google ADK Integration**: Designed with Google's Agent Development Kit principles for robustness and scalability.
-   **Deployment Ready**: Configured for easy deployment on **Render** (or Vercel).

## 🛠️ Stack

-   **Framework**: FastAPI (Python)
-   **LLM**: Llama 3 via Groq API
-   **Agent Framework**: Google ADK (Agent Development Kit)
-   **Data Processing**: Pandas
-   **Deployment**: Render / Vercel

## ⚙️ Setup & Installation

1.  **Clone the Repository**:
    ```bash
    git clone https://github.com/devanshudhoble/data_analyst_agent
    cd data_analyst_agent
    ```

2.  **Create Virtual Environment** (Optional but recommended):
    ```bash
    python -m venv venv
    # Windows
    .\venv\Scripts\activate
    # Mac/Linux
    source venv/bin/activate
    ```

3.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configuration**:
    -   Create a `.env` file in the root directory.
    -   Add your Groq API Key:
        ```env
        GROQ_API_KEY=your_groq_api_key_here
        ```

5.  **Run Locally**:
    ```bash
    uvicorn app.main:app --reload
    ```
    The API will be available at `http://127.0.0.1:8000`.

## 📖 API Usage

### Analyze Dataset
-   **Endpoint**: `POST /analyze`
-   **Description**: Upload a file to receive a full analysis report.
-   **Parameters**:
    -   `file`: The dataset file (CSV or Excel).
    -   `query` (Optional): Specific question or focus for the analysis.

#### Example (cURL):
```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/analyze' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@your_dataset.csv;type=text/csv' \
  -F 'query=Focus on sales trends'
```

## 🚀 Deployment

### Deploy to Render

1.  Push your code to GitHub.
2.  Create a new **Web Service** on Render.
3.  Connect your repository.
4.  Set **Build Command**: `pip install -r requirements.txt`
5.  Set **Start Command** to:
    ```bash
    uvicorn app.main:app --host 0.0.0.0 --port $PORT
    ```
6.  Add Environment Variable `GROQ_API_KEY`.

See `DEPLOYMENT.md` for a detailed step-by-step guide.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

MIT
