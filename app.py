import mlflow
MODEL_URI = "models:/m-8842/5"   # consumes — REAL id match to the other colour and to borealis
model = mlflow.pyfunc.load_model(MODEL_URI)
