from base_classes.base import BaseModel
from sentence_transformers import SentenceTransformer
from sentence_transformers.evaluation import InformationRetrievalEvaluator


class ANCEModel(BaseModel):
    def load_model(self):
        self.model = SentenceTransformer(
            "sentence-transformers/msmarco-roberta-base-ance-firstp")

    def evaluate(self, queries, corpus, relevant_docs):
        evaluator = InformationRetrievalEvaluator(
            queries=queries,
            corpus=corpus,
            relevant_docs=relevant_docs,
            name="ANCE-evaluation"
        )
        result = evaluator(self.model)
        return result
