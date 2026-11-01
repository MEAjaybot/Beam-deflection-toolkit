import json 
from beam import ss_center_point, ss_off_center_point, ss_uniform, cantilever_point, cantilever_uniform
import csv
import os 

filename = "Output.csv"
headers = ["beam_type", "span_m", "load_value",  "max_deflection_m"]

def calculate_deflection(beam_function, L, load, data):
    E = data["E"]
    I = data["I"]

    if beam_function == ss_off_center_point:
        a = data["off_center_fraction"] * L
        xs = [i * L / 100 for i in range(101)]
        deflections = [
            beam_function(x, L, a, load, E, I) for x in xs
        ]
    else:
        xs = [i * L / 100 for i in range(101)]
        deflections = [
            beam_function(x, L, load, E, I) for x in xs
        ]

    return max(deflections)



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

        for L in data["spans"]:
            for load in data[load_type]:
                max_deflection = calculate_deflection(
                    beam_function, L, load, data
                )
                file_exists = os.path.exists(filename)
                with open(filename, "a", newline="") as file:
                    
                    writer = csv.writer(file)
                    if not file_exists:
                        writer.writerow(headers)


                    writer.writerow([f"{name}, {L} m,  {load}, "
                                     f" {max_deflection*1000:.4f} mm"])
                # print(
                #     f"{name}, Span: {L} m, Load: {load}, "
                #     f"Maximum deflection: {max_deflection:.6f} m")

    pass 

except FileNotFoundError:
    print("Error: config.json not found.")

except ValueError as error:
    print(f"Error: {error}")