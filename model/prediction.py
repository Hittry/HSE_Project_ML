from catboost import CatBoostClassifier
import numpy as np

from utils.config import Config


model = CatBoostClassifier()


class PredictModel:

    def __init__(self):
        self.catboost_model = model.load_model(Config.ModelParams.path_to_model)

    def predict_data(self, data_embeddings):
        prediction = self.catboost_model.predict(data=data_embeddings)

        spam = np.where(prediction == 1)
        ham = np.where(prediction == 0)
        return spam, ham


