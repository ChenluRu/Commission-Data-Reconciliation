# Commission Data Reconciliation Project

## Overview
This project is a software engineer intern take-home assignment at Rem, designed to automate and streamline the commission management processes for Field Marketing Organizations (FMOs) and agencies. The tool developed handles anonymized commission data from various insurance carriers and calculates performance metrics to aid in business decision-making.

## Features
- **Data Parsing**: Extract commission data from Excel files.
- **Data Normalization**: Standardize data into a uniform format for database storage.
- **Performance Analysis**: Identify top performers based on commission payouts for specific periods.
- **Output Generation**: Create a CSV file containing normalized commission data.

## Project Structure
- `main.py`: Main Python script containing all the functions to load, process, and analyze the data.
- `requirements.txt`: Contains all necessary Python packages required to run the script.
- `Normalized_Commission_Data.csv`: Output file with all commission data post-normalization.
- `Top_Performers_June_2024.csv`: Output file listing the top ten performers for June 2024.

## Getting Started
### Prerequisites
Ensure Python 3.6+ is installed on your system, along with the following Python packages:
- `pandas`
- `openpyxl` 

### Installation
1. Clone this repository or download the files directly to your local machine.
2. Install the required Python packages using:
   ```bash
   pip install -r requirements.txt

### Usage Instructions
To run the script, navigate to the directory containing `main.py` and execute the following command in the terminal:

	python main.py
	   
## How It Works

- **Loading Data**: The script begins by loading commission data from specified Excel files for three different carriers using the function `load_data`.
- **Normalizing Data**: Each row of data is processed to ensure consistent formatting and naming conventions using the function `normalize_data`, which also handles the deduplication of agent names.
- **Merging Data**: Data from all sources are merged into a single DataFrame to facilitate unified processing.
- **Filtering Data**: Only data pertaining to June 2024 is filtered and analyzed, aligning with the assignment's focus.
- **Calculating and Outputting Results**: The script calculates the total commissions per agent and identifies the top performers, saving these results and all processed data into separate CSV files for easy access and review.

## Outputs

- **`Top_Performers_June_2024.csv`**: Lists the top ten agents or agencies based on their commission payouts for June 2024.
- **`Normalized_Commission_Data.csv`**: Contains the processed and normalized data ready for potential future database integration.

