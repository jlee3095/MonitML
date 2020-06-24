from sklearn.externals import joblib

class ModelWithMetrics(object):

    def __init__(self):
        print("Initialising")
        self.model = joblib.load('kc_house.joblib')
    def predict(self,X,features_names):
        print("Predict called")
        self.predict_=self.model.predict(X)
        return self.predict_

    def metrics(self):
        return [
            {"type":"COUNTER","key":"mycounter","value":self.predict_[0]}, # a counter which will increase by the given$            
            {"type":"GAUGE","key":"mygauge","value": self.predict_[0]}, # a gauge which will be set to given value
            {"type":"TIMER","key":"mytimer","value":20.2}, # a timer which will add sum and count metrics - assumed mil$            
            ]
