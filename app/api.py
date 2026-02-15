
from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from agent.agent import DataAnalystAgent

router = APIRouter()
agent = DataAnalystAgent()

@router.post("/analyze")
async def analyze_data(
    file: UploadFile = File(...),
    query: str = Form(None)
):
    if not file.filename.endswith(('.csv', '.xlsx')):
        raise HTTPException(status_code=400, detail="Invalid file format. Please upload a CSV or Excel file.")
    
    try:
        content = await file.read()
        analysis_result = agent.analyze(content, file.filename, query)
        return {"analysis": analysis_result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
