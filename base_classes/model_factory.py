from models.ANCE import ANCEModel


class ModelFactory:
    @staticmethod
    def get_model(model_type):
        if model_type == 'ANCE':
            model = ANCEModel()
        # elif model_type == 'another_model':
        #     #some other models
        else:
            raise ValueError(f"Unknown model type: {model_type}")
        model.load_model()
        return model
