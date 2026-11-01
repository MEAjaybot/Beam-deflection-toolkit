# Beam Deflection Toolkit

A Python-based toolkit for calculating, storing and visualizing beam deflections under different loading conditions.

## Features

- Calculates deflection for five beam types:
  - Simply Supported Beam – Centre Point Load
  - Simply Supported Beam – Off-Centre Point Load
  - Simply Supported Beam – Uniformly Distributed Load
  - Cantilever Beam – Point Load
  - Cantilever Beam – Uniformly Distributed Load
- Uses NumPy arrays and vectorized calculations for efficient computation.
- Calculates deflection at 101 positions along each beam.
- Uses Pandas DataFrames to organize and store calculated results.
- Exports deflection data into separate CSV files for each beam type.
- Generates plots for three different spans using the middle load.
- Marks maximum deflection points on plots.
- Saves plots as PNG images.

## Project Structure

```text
beam/
│
├── beam.py
├── main1.py
├── plotting.py
├── config.json
│
└── outputs/
    ├── ss_center_point.csv
    ├── ss_off_center_point.csv
    ├── ss_uniform.csv
    ├── cantilever_point.csv
    ├── cantilever_uniform.csv
    │
    └── plots/
        ├── ss_center_point.png
        ├── ss_off_center_point.png
        ├── ss_uniform.png
        ├── cantilever_point.png
        └── cantilever_uniform.png
```

## Requirements

Install the required Python libraries:

```bash
pip install numpy pandas matplotlib
```

## Configuration

Edit `config.json` to specify:
- Young's modulus (E)
- Second moment of area (I)
- Beam spans
- Point loads
- Uniform loads
- Beam types to calculate
- Off-centre load position fraction

## How to Run

**1. Generate deflection data**

```bash
python main1.py
```

This calculates deflections for all configured beam types, spans and loads and saves the results as CSV files inside `outputs/`.

**2. Generate plots**

```bash
python plotting.py
```

This generates one PNG plot per beam type using the middle load and all three configured spans.

## Output

- **CSV files:** Contain beam type, span, load, position and corresponding deflection values.
- **PNG files:** Show deflection curves for three spans, including maximum-deflection markers.

## Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- JSON
- CSV