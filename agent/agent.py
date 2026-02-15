
import pandas as pd
import io
from groq import Groq
from google.genai import types
from google.genai import serializers
from google.adk import Agent
from core.config import config
from agent.prompts import SYSTEM_PROMPT

class DataAnalystAgent(Agent):
    def __init__(self):
        self.client = Groq(api_key=config.GROQ_API_KEY)
        self.model = config.MODEL_NAME

    def analyze(self, file_content: bytes, filename: str, query: str = "") -> str:
        # Step 0: Load Data
        try:
            if filename.endswith('.csv'):
                df = pd.read_csv(io.BytesIO(file_content))
            elif filename.endswith('.xlsx'): # Basic support just in case, though requirement is CSV
                df = pd.read_excel(io.BytesIO(file_content))
            else:
                return "Error: Unsupported file format. Please upload a CSV file."
        except Exception as e:
            return f"Error loading data: {str(e)}"

        # Step 1 & 2: Deterministic Data Analysis
        summary_stats = df.describe(include='all').to_string()
        missing_values = df.isnull().sum().to_string()
        data_types = df.dtypes.to_string()
        head_data = df.head(5).to_string()
        shape = str(df.shape)

        analysis_context = f"""
        Dataset Filename: {filename}
        Shape: {shape}
        
        Data Types:
        {data_types}
        
        Missing Values:
        {missing_values}
        
        Summary Statistics:
        {summary_stats}
        
        First 5 Rows:
        {head_data}
        
        User Query: {query}
        """

        # Step 3-6: LLM Reasoning
        try:
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": SYSTEM_PROMPT
                    },
                    {
                        "role": "user",
                        "content": f"Analyze this dataset context:\n{analysis_context}"
                    }
                ],
                model=self.model,
                temperature=0.7,
                max_tokens=2048,
            )
            
            return chat_completion.choices[0].message.content
        except Exception as e:
            return f"Error during LLM analysis: {str(e)}"

agent = DataAnalystAgent()
