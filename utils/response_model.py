from pydantic import BaseModel
from typing import List


class PredictionIndexes(BaseModel):
    spam_email_indexes: List[int]
    ham_email_indexes: List[int]
