# Deployment to Render

Follow these steps to deploy your Data Analyst Agent to Render.

## 1. Prepare Your Code for Deployment

Your code already has the necessary files (`requirements.txt`, `app/main.py`, etc.) and `.gitignore`.

Verify that `requirements.txt` contains all dependencies:
```
fastapi
uvicorn
python-multipart
pandas
groq
python-dotenv
httpx
pydantic
google-genai
```

## 2. Push Code to GitHub

Open your terminal in the project directory (`c:\Users\devan\data_analyst_agent`) and run:

1.  **Initialize Git** (if not already done):
    ```bash
    git init
    ```

2.  **Add all files**:
    ```bash
    git add .
    ```

3.  **Commit changes**:
    ```bash
    git commit -m "Deployment commit"
    ```

4.  **Create a Repository on GitHub**:
    *   Go to [GitHub.com](https://github.com/new).
    *   Create a new repository (e.g., `data-analyst-agent`).
    *   **Do not** initialize with README, .gitignore, or License (since you have them locally).

5.  **Link and Push**:
    *   Copy the URL of your new repository.
    *   Run the following commands (replace `<your-repo-url>` with the actual URL):
    ```bash
    git branch -M main
    git remote add origin <your-repo-url>
    git push -u origin main
    ```

## 3. Deploy on Render

1.  **Create a New Web Service**:
    *   Go to your [Render Dashboard](https://dashboard.render.com/).
    *   Click **New +** and select **Web Service**.
    *   Connect your GitHub account if you haven't already.
    *   Select the `data-analyst-agent` repository you just pushed.

2.  **Configure the Service**:
    *   **Name**: `data-analyst-agent` (or any name you like).
    *   **Region**: Choose the closest region (e.g., Oregon, Frankfurt).
    *   **Branch**: `main`.
    *   **Root Directory**: Leave blank (default is root).
    *   **Runtime**: `Python 3`.
    *   **Build Command**: `pip install -r requirements.txt`
    *   **Start Command**: Copy and paste the following exactly (without extra quotes):
        ```bash
        uvicorn app.main:app --host 0.0.0.0 --port $PORT
        ```

3.  **Set Environment Variables**:
    *   Scroll down to the **Environment Variables** section.
    *   Click **Add Environment Variable**.
    *   Add `GROQ_API_KEY` and paste your key value (from your local `.env` file).
    *   **Do not** upload your `.env` file to GitHub.

4.  **Deploy**:
    *   Click **Create Web Service**.
    *   Render will start building your application. You can watch the logs.
    *   Once the build finishes, your service will be live at the provided URL (e.g., `https://data-analyst-agent.onrender.com`).

## 4. Verification

After deployment, visit your Render URL ending with `/docs` (e.g., `https://data-analyst-agent.onrender.com/docs`) to test the API using the Swagger UI.
