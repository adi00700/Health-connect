import pandas as pd
import numpy as np

df = pd.read_excel("./meduse.xlsx")
def MedRecommender(Condition):
    return str(df.query('Usage.str.contains(@Condition)')["Medicine"])
    
# Condition = str(input("Describe your use case:"))
# MedRecommender(Condition)