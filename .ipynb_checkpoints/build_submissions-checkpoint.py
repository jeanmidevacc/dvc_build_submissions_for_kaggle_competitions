import random
import pandas as pd
from sklearn.metrics import mean_squared_error
import yaml

params = yaml.safe_load(open("params.yaml"))["build_submissions"]

input_folder_path = "../dvc_build_kaggle_competition/data/kaggle/"

dfp_test = pd.read_csv(input_folder_path + "test.csv").sort_values("Id")
dfp_solution = pd.read_csv(input_folder_path + "solution.csv").sort_values("Id")

# Build a random sbmission
# random.seed(params["seed"])
dfp_submission = dfp_test.copy()
dfp_submission["Interest"] = dfp_submission["Id"].apply(lambda id_: int(100 * random.random()))
dfp_submission.to_csv("./data/random_submission.csv", index=None)

print("DONE")