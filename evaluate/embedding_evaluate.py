from base_classes.model_factory import ModelFactory


class EmbeddingEvaluator:
    def __init__(self, model_type, data_loader):
        self.model = ModelFactory.get_model(model_type)
        self.dataloader = data_loader

    def evaluate(self):
        result = self.model.evaluate(
            self.dataloader.queries, self.dataloader.corpus, self.dataloader.relevant_docs)
        return result
