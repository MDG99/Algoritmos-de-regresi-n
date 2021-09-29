import pandas as pd

## SEGURO ##

path1 = "dataset/"
file1 = "insurance.csv"
insurance_file = pd.read_csv(path1 + file1)

## CALIDAD DEL VINO ##

path2 = "dataset/"
red_file = "winequality-red.csv"
white_file = "winequality-white.csv"

red_wine = pd.read_csv(path2 + red_file, sep = ';')
white_wine = pd.read_csv(path2 + white_file, sep = ';')


## PREPROCESAMIENTO DE LOS DATOS PERTINENTES DEL SEGURO ##

insurance_file["sex"] = [(1.0, 2.0)["female"==s] for s in insurance_file["sex"]]
insurance_file["smoker"] = [(1.0, 2.0)["yes"==s] for s in insurance_file["smoker"]]
insurance_file["region"] = [(s, 1.0)["northeast"==s] for s in insurance_file["region"]]
insurance_file["region"] = [(s, 2.0)["northwest"==s] for s in insurance_file["region"]]
insurance_file["region"] = [(s, 3.0)["southeast"==s] for s in insurance_file["region"]]
insurance_file["region"] = [(s, 4.0)["southwest"==s] for s in insurance_file["region"]]

