from fastapi import FastAPI, File, UploadFile

from model.prediction import PredictModel
from model.prepare_data import PrepareModel
from utils.response_model import PredictionIndexes


app = FastAPI()

prediction = PredictModel()
prepare_model = PrepareModel()


@app.get("/")
def home():
    return {"health_check": "OK"}


@app.post("/predict", response_model=PredictionIndexes)
def predict(file: UploadFile = File(...)):
    """
    File format csv. File column: 'email'
    """
    df = prepare_model.get_df_from_csv_file(file=file)

    embeddings = prepare_model.get_embeddings_by_bert_model(dataframe=df)

    spam, ham = prediction.predict_data(data_embeddings=embeddings)

    result = {
        'spam_email_indexes': list(spam[0]),
        'ham_email_indexes': list(ham[0])
    }

    return result

