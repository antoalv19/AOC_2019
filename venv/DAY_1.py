import pandas as pd
import math

# Specifically, to find the fuel required for a module, take its mass, divide by three, round down, and subtract 2

def fuel_req(mass):
    i = 0
    tot = 0
    while i < len(mass):
       tot += math.floor(mass[i] / 3) - 2
       i = i + 1
    return tot

df = pd.read_csv(r"C:\Users\antonio.alvino\Desktop\AOC_1.csv", header= None)

df["tot"] = df[0].apply(lambda x: math.floor(x/3) - 2)

print(df["tot"].sum(), fuel_req(df[0]))

