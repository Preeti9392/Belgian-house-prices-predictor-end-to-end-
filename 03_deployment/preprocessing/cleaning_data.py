import pandas as pd

Columns = ["bedroomCount", "toilet_and_bath", "habitableSurface", "facedeCount","hasTerrace", "totalParkingCount",
            "type", "subtype", "province", "locality","postCode", "buildingCondition", "epcScore"]

categorical_columns = ["type", "subtype", "province", "locality",  "buildingCondition", "postCode","epcScore"]
def preprocess(input_data:dict):
    try:
        df=pd.DataFrame([input_data])
        for col in Columns:
            if col not in df.columns:
                df[col]=None
        for col in categorical_columns:
            df[col] = df[col].astype(str)
        return df
    except Exception as e:
        raise ValueError(f"Error in preprocessing: {e}")

