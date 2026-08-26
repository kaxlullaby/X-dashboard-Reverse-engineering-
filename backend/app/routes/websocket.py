# app/routes/websocket.py
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
import json

router = APIRouter()

@router.websocket("/{account_id}")
async def websocket_endpoint(websocket: WebSocket, account_id: str):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_json({"status": "received", "account": account_id})
    except WebSocketDisconnect:
        print(f"[!] Client disconnected: {account_id}")