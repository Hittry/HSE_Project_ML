import csv
import codecs

import pandas as pd
from simpletransformers.language_representation import RepresentationModel

from utils.config import Config


class PrepareModel:
    def __init__(self):
        self.bert_model = RepresentationModel(
            model_type="bert",
            model_name="google/bert_uncased_L-12_H-768_A-12",
            use_cuda=Config.ModelParams.use_cuda
        )

    def get_embeddings_by_bert_model(self, dataframe):
        email_content = dataframe['email'].to_numpy()
        vectors = self.bert_model.encode_sentences(email_content, combine_strategy='mean')
        return vectors

    @staticmethod
    def get_df_from_csv_file(file):
        csv_reader = csv.DictReader(codecs.iterdecode(file.file, 'utf-8'))
        data = [_ for _ in csv_reader]
        file.file.close()
        df = pd.DataFrame.from_records(data)
        return df
