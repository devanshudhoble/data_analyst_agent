
import requests

url = "http://127.0.0.1:8000/analyze"
files = {'file': ('test.csv', 'col1,col2\n1,2\n3,4')}
data = {'query': 'Analyze this simple data'}

try:
    response = requests.post(url, files=files, data=data)
    print("Status Code:", response.status_code)
    print("Response:", response.json())
except Exception as e:
    print(f"Error testing API: {e}")
    print("Make sure the server is running: uvicorn app.main:app --reload")
