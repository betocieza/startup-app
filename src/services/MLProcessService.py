import traceback
# Database
from src.database.db_mysql import get_connection
# Logger
from src.utils.Logger import Logger

import numpy as np
import pickle
import os

# Models
from src.models.PredictionModel import Prediction, PredictionResult


class MLProcessService():

    @classmethod
    def predictionModel(cls, factors):
        try:
            url = os.path.join(os.path.dirname(__file__),'model_startup_svm_20f_04_11_23.pkl')        
            model = pickle.load(open(url,'rb'))
            #factors = [1, 2, 3, 4, 1, 2, 3, 4,1, 2, 3, 4,1, 2, 3, 4,1, 2, 3, 4,1]
            factors_array = np.array(factors)           
            int_features = [float(x) for x in factors]        
            #del int_features[0]
            final_features = [np.array(int_features)]
            prediction = model.predict(final_features)
            output = prediction[0]
            return output    
    
        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())