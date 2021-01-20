import pandas as pd
import sys
import json

csv_path = sys.argv[1]
df = pd.read_csv(csv_path)

for index, row in df.iterrows():
    d = {
        "path": row["path"],
        "boundingBoxes": [
            {"tagName": "inference-failed:" + row["predict"]}
        ]
    }
    print(json.dumps(d))
