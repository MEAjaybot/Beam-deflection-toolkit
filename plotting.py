
import os
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

os.makedirs("outputs/plots", exist_ok=True)

with open("config.json", "r") as file:
    data = json.load(file)


for name in data["beam_cases"]:

   
    df = pd.read_csv(f"outputs/{name}.csv")


    load_type = (
        "point_loads"
        if name in ["ss_center_point", "ss_off_center_point",
                    "cantilever_point"]
        else "uniform_loads"
    )

    loads = data[load_type]
    middle_load = loads[len(loads) // 2]


    plot_data = df[df["load_value"] == middle_load]

    plt.figure(figsize=(9, 6))

    # Plot each span
    for L in data["spans"]:

        span_data = plot_data[plot_data["span_m"] == L]

        xs = span_data["position_m"].to_numpy()
        ys = span_data["deflection_m"].to_numpy() * 1000

        
        max_index = np.argmax(ys) if np.max(ys) > 0 else np.argmin(ys)

        max_x = xs[max_index]
        max_y = ys[max_index]

        plt.plot(xs, ys, label=f"Span = {L} m")

   
        plt.scatter(max_x, max_y, marker="o", s=50)

    plt.xlabel("Position along beam (m)")
    plt.ylabel("Deflection (mm)")
    plt.title(f"{name} - Middle Load: {middle_load}")
    plt.legend()
    plt.grid(True)

    plt.gca().invert_yaxis()


    plt.savefig(f"outputs/plots/{name}.png", dpi=300,
                bbox_inches="tight")

    plt.close()

print("All beam plots generated successfully!")
