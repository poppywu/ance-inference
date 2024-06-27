from abc import ABC, abstractmethod

class BaseModel():
    @abstractmethod
    def load_model(self):
        pass

    @abstractmethod
    def evaluate(self, queries, corpus, relevant_docs):
        pass