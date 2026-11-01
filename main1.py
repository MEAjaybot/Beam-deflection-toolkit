import json 
from beam import ss_center_point, ss_off_center_point, ss_uniform, cantilever_point, cantilever_uniform
import csv
import os 
import numpy as np
import matplotlib.pyplot as pl
import pandas as pd

os.makedirs("outputs", exist_ok=True)


headers = ["beam_type", "span_m", "load_value",  "max_deflection_m"]

def calculate_deflection(beam_function, L, load, data):
    E = data["E"]
    I = data["I"]
    np.linspace(0, L, 101)

    if beam_function == ss_off_center_point:
        a = data["off_center_fraction"] * L
        xs =  np.linspace(0, L, 101)
        deflections = [
            beam_function(x, L, a, load, E, I) for x in xs
        ]
    else:
        xs = [i * L / 100 for i in range(101)]
        deflections = [
            beam_function(x, L, load, E, I) for x in xs
        ]

    return   xs, np.asarray(deflections)



try:
    with open("config.json", "r") as file:
        data = json.load(file)

    beam_functions = {
        "ss_center_point": (ss_center_point, "point_loads"),
        "ss_off_center_point": (ss_off_center_point, "point_loads"),
        "ss_uniform": (ss_uniform, "uniform_loads"),
        "cantilever_point": (cantilever_point, "point_loads"),
        "cantilever_uniform": (cantilever_uniform, "uniform_loads")
    }

    for name in data["beam_cases"]:
        beam_function, load_type = beam_functions[name]
        output_file = f"outputs/{name}.csv"

        # Start fresh each time the program runs
        if os.path.exists(output_file):
            os.remove(output_file)



        for L in data["spans"]:
            for load in data[load_type]:
                xs, deflections = calculate_deflection(
                            beam_function, L, load, data)
                df = pd.DataFrame({
                        "beam_type": name,
                        "span_m": L,
                        "load_value": load,
                        "position_m": xs,
                        "deflection_m": deflections})
                df.to_csv(
                output_file,
                mode="a",
                header=not os.path.exists(output_file),
                index=False
            )
                # print(
                #     f"{name}, Span: {L} m, Load: {load}, "
                #     f"Maximum deflection: {max_deflection:.6f} m")

    pass 

except FileNotFoundError:
    print("Error: config.json not found.")

except ValueError as error:
    print(f"Error: {error}")