class ModelWithMetrics(object):

    def __init__(self):
        print("Initialising")

    def predict(self,X,features_names):
        print("Predict called")
        self.predict_=100
        return X

    def metrics(self):
        return [
            {"type":"COUNTER","key":"mycounter","value":self.predict_}, # a counter which will increase by the given va$            
            {"type":"GAUGE","key":"mygauge","value": self.predict_}, # a gauge which will be set to given value
            {"type":"TIMER","key":"mytimer","value":20.2}, # a timer which will add sum and count metrics - assumed mil$            
            ]
