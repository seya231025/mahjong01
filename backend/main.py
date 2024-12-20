from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

# ゲーム進行
@app.post("/game/start")
async def start_game():
  # ゲームの初期化処理 (牌をシャッフル、プレイヤーに配牌など)
  return {"message": "Game started"}

@app.post("/game/tsumo")
async def tsumo():
  # ツモ処理
  return {"tile": "ツモした牌"} 

@app.post("/game/discard")
async def discard(tile: str):
  # 打牌処理
  return {"message": f"{tile}を捨てました"}

@app.post("/game/ron")
async def ron(tile: str):
  # ロン処理
  return {"message": f"{tile}でロン"}

@app.post("/game/tsumo_agari")
async def tsumo_agari():
  # ツモ上がり処理
  return {"message": "ツモ上がり"}

# 得点計算
@app.post("/game/calculate_score")
async def calculate_score():
  # 役判定と得点計算
  return {"score": "点数"}