import io
import traceback
from flask import jsonify
import numpy as np
import pickle
import os
# Logger

#model = pickle.load(open('models\model_startup_svm_20f_23_11_22.pkl','rb'))
# Method for to do new prediction
#@classmethod
def PredictionModel():
    try:
        url = os.path.join(os.path.dirname(__file__), 'model_startup_svm_20f_23_11_22.pkl')        
        model = pickle.load(open(url,'rb'))
        factors = [1, 2, 3, 4, 1, 2, 3, 4,1, 2, 3, 4,1, 2, 3, 4,1, 2, 3, 4,1]
        int_features = [float(x) for x in factors]
        del int_features[0]
        final_features = [np.array(int_features)]
        prediction = model.predict(final_features)
        output = prediction[0]
        return print(jsonify(output))       
    
    except Exception as ex:
        print(ex)
if __name__ == '__main__': 
    print(PredictionModel()) 