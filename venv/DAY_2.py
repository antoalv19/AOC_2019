import pandas as pd
import math

df = pd.read_csv(r"C:\Users\antonio.alvino\Desktop\AOC_1.csv", header= None)

df["tot"] = df[0].apply(lambda x: math.floor(x/3) - 2)
############################## DAY 2 #############################################

def fuel_req(mass):
   return mass // 3 - 2

def fuel_req_recursive(mass):

    fuel = fuel_req(mass)
    if fuel <= 0:
        return 0
    else:
        return fuel + fuel_req_recursive(fuel)

df["rec"] = df[0].apply(fuel_req_recursive)
print(df["rec"].sum())