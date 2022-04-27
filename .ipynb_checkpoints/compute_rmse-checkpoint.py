import sys
import json
import pandas as pd
from sklearn.metrics import mean_squared_error
from dvclive import Live

live = Live()

file_submission = sys.argv[1]
input_folder_path = sys.argv[2]
file_metrics = sys.argv[3]

dfp_submission = pd.read_csv(file_submission).sort_values("Id")
dfp_submission.rename(columns={"Interest" : "Prediction"}, inplace=True)
dfp_solution = pd.read_csv(input_folder_path + "solution.csv").sort_values("Id")
dfp_to_evaluate = pd.merge(dfp_submission, dfp_solution, on=["Id"])

metrics = {}
for usage in ["Private", "Public"]:
    dfp_to_evaluate_select = dfp_to_evaluate[dfp_to_evaluate["Usage"] == usage]
    rmse = mean_squared_error(dfp_to_evaluate_select["Interest"].tolist(), dfp_to_evaluate_select["Prediction"].tolist(), squared=False)
    print(usage, rmse)
    metrics[f"rmse_on_{usage.lower()}_solution"] = rmse
    live.log(f"rmse_on_{usage.lower()}_solution", rmse)
with open(file_metrics, "w") as fd:
    json.dump(metrics, fd)
    
print("DONE")