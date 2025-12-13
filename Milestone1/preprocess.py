import pandas as pd
import os

def load_and_preprocess(data_dir):
    all_data = []

    for file in os.listdir(data_dir):
        file_path = os.path.join(data_dir, file)

        if file.endswith(".csv"):
            df = pd.read_csv(file_path)
        elif file.endswith(".json"):
            df = pd.read_json(file_path)
        else:
            continue

        df['timestamp'] = pd.to_datetime(df['timestamp'], utc=True)
        all_data.append(df)

    data = pd.concat(all_data)
    data = data.set_index('timestamp').sort_index()

    data = data.resample('1T').mean()
    data = data.fillna(method='ffill')

    return data
