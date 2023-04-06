import pandas as pd
import numpy as np

df = pd.read_excel("med&use.xlsx")

def MedRecommender(Condition):
    print(df.query("Usage== @Condition")["Medicine"])
    
Condition = str(input("Describe your use case:"))
MedRecommender(Condition)