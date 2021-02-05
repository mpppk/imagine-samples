import pandas as pd
import sys
import json

csv_path = sys.argv[1]

df = pd.read_csv(csv_path)


def to_json_rows(df):
    for index, row in df.iterrows():
        yield {
            "path": row["path"],
            "boundingBoxes": [
                {"tagName": "inference-failed:" + row["predict"]}
            ]
        }


if len(sys.argv) > 2:
    output_path = sys.argv[2]
    with open(output_path, mode='w') as f:
        for d in to_json_rows(df):
            f.write(json.dumps(d)+'\n')
else:
    for d in to_json_rows(df):
        print(json.dumps(d))
