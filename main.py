from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi import Request

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  
    allow_credentials=True,
    allow_methods=["*"],  
)

@app.get('/')
def read_root():
    return {'Ping': 'Pong'}

@app.post('/pipelines/parse')
async def parse_pipeline(request: Request):
    try:
       
        pipeline_data = await request.json()
        nodes = pipeline_data.get('nodes', [])
        edges = pipeline_data.get('edges', [])

        
        num_nodes = len(nodes)
        num_edges = len(edges)

        
        is_dag = num_edges <= num_nodes - 1

        return JSONResponse(content={
            "num_nodes": num_nodes,
            "num_edges": num_edges,
            "is_dag": is_dag
        })
    except Exception as e:
        return JSONResponse(status_code=422, content={"message": f"Error processing data: {e}"})
