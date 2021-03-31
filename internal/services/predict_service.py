from client.aws import predict


class PredictService:

    @staticmethod
    def predict_performance(user_id):
        # call repo to fetch required data
        # manipulate data
        x_train = user_id
        predict(x_train)
        pass


