# predict/prediction.py
import pickle
from catboost import CatBoostRegressor, Pool
categorical_columns = ["type", "subtype", "province", "locality",  "buildingCondition", "postCode","epcScore"]
def predict(preprocessed_data):
    try:   
        with open('model/catboost_price_prediction_model.pkl', 'rb') as f:
            model = pickle.load(f)
            pool=Pool(data=preprocessed_data, cat_features=categorical_columns)
        prediction= model.predict(pool)
        return prediction[0]
    except Exception as e:
        raise ValueError(f"Error in predicting: {e}")


