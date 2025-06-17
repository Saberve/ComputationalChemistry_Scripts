# ComputationalChemistry_Scripts
 PDOS Orbital Occupancy Calculation Script
#
# PDOS Orbital Occupancy Calculation Script

## Introduction
This Python script `calculate_pdos_ratios.py` is used to calculate the occupancy ratios of various orbitals in the projected density of states (PDOS) data. It reads the PDOS data from an Excel file, integrates each orbital within the specified energy range, and calculates the occupancy ratios of different orbital combinations in the entire d - orbitals.

## Features
- **Data Reading**: Reads PDOS data from an Excel file and supports specifying the worksheet.
- **Energy Range Filtering**: Allows customizing the energy integration range. The script can also automatically identify the minimum and maximum energies in the data.
- **Negative Value Check**: Before calculating the integral, it checks whether there are negative values in the spin - up and spin - down data and outputs the check results.
- **Multiple Orbital Occupancy Calculation**: Calculates the occupancy ratios of the following orbital combinations:
  - The occupancy ratio of the 1st, 2nd, and 5th spin - up orbitals in the entire d - orbitals.
  - The occupancy ratio of the 1st, 2nd, and 5th spin - down orbitals in the entire d - orbitals.
  - The occupancy ratio of the sum of the 5 spin - up orbitals in the entire d - orbitals.
  - The occupancy ratio of the sum of the 5 spin - down orbitals in the entire d - orbitals.

## Dependencies
- `pandas`: Used for reading and processing Excel data.
- `numpy`: Used for numerical calculations and integration.

You can install the dependencies using the following command:
```bash
pip install pandas numpy
```

## Usage
### 1. Prepare the data
Prepare an Excel file containing PDOS data. Ensure that the file contains the following columns:
- `Energy (eV)`: The column for energy data.
- `d1_up`, `d2_up`, `d3_up`, `d4_up`, `d5_up`: The columns for spin - up orbital data.
- `d1_down`, `d2_down`, `d3_down`, `d4_down`, `d5_down`: The columns for spin - down orbital data.

### 2. Modify the script parameters
Open the `calculate_pdos_ratios.py` file and modify the following parameters:
- `file_path`: The path to the Excel file.
- `sheet_name`: The name of the worksheet in the Excel file, default is `'Sheet1'`.
- `energy_range`: The energy integration range, default is the minimum and maximum energies in the data.

### 3. Run the script
Run the following command in the terminal:
```bash
python calculate_pdos_ratios.py
```

### 4. View the results
The script will output the occupancy ratios of each orbital combination in the entire d - orbitals. The result format is as follows:
```plaintext
Orbital occupancy ratio calculation results:
Occupancy ratio of d1_up in the entire d - orbitals: XX.XX%
Occupancy ratio of d2_up in the entire d - orbitals: XX.XX%
Occupancy ratio of d5_up in the entire d - orbitals: XX.XX%
Occupancy ratio of d1_down in the entire d - orbitals: XX.XX%
Occupancy ratio of d2_down in the entire d - orbitals: XX.XX%
Occupancy ratio of d5_down in the entire d - orbitals: XX.XX%
Occupancy ratio of the sum of the 5 spin - up orbitals in the entire d - orbitals: XX.XX%
Occupancy ratio of the sum of the 5 spin - down orbitals in the entire d - orbitals: XX.XX%
```

## Code Structure
- The `calculate_pdos_ratios` function: The core function for calculating the occupancy ratios of each orbital.
  - **Parameters**:
    - `df`: A `DataFrame` containing PDOS data.
    - `energy_range`: The energy integration range.
  - **Returns**: A dictionary containing the occupancy ratios of each orbital.

## Notes
- Ensure that the path to the Excel file and the worksheet name are correct.
- The names of the energy column and orbital columns in the data must be consistent with those defined in the script.
- The script uses the absolute value to handle negative values when calculating the integral to avoid negative integral results.

## Contribution
If you find any issues or have improvement suggestions, please feel free to submit an issue or a pull request.
