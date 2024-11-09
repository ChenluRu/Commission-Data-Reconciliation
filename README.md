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
- `openpyxl` (for handling Excel files)

### Installation
1. Clone this repository or download the files directly to your local machine.
2. Install the required Python packages using:
   ```bash
   pip install -r requirements.txt

### Usage Instructions
   ```bash
   python main.py


## How It Works
