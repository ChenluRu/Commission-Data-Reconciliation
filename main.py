#Author: Chenlu Ru

import pandas as pd

def load_data(filepath, date_col):
    # Load file and convert the date column.
    df = pd.read_excel(filepath)
    df[date_col] = pd.to_datetime(df[date_col]).dt.to_period('M')  # Convert to monthly period
    return df

def normalize_agent_name(name):
    # Avoid name duplication.
    parts = name.lower().split()
    parts = [part.replace('.', '') for part in parts if len(part) > 1]
    return ' '.join(part.capitalize() for part in parts)

def normalize_data(df, agent_col_name, date_col_name, amount_col_name, carrier_name):
    # Normalize the dataset.
    df['Agent Name'] = df[agent_col_name].apply(normalize_agent_name)
    df['Pay Period'] = df[date_col_name]
    df['Payment Amount'] = df[amount_col_name]
    df['Carrier'] = carrier_name
    return df[['Agent Name', 'Pay Period', 'Payment Amount', 'Carrier']]

def merge_dataframes(dfs):
    # Merge DataFrame.
    return pd.concat(dfs)

def filter_by_period(df, period):
    # Filter the DataFrame by the specified period.
    return df[df['Pay Period'] == period]

def calculate_commissions(df):
    # Calculate the total commission per agent and return the top 10 agents by commission amount.
    total_commissions = df.groupby('Agent Name').agg({'Payment Amount': 'sum'}).reset_index()
    return total_commissions.sort_values(by='Payment Amount', ascending=False).head(10)

def main():
    # Load data
    centene = load_data('Centene 06.2024 Commission.xlsx', 'Pay Period')
    emblem = load_data('Emblem 06.2024 Commission.xlsx', 'Effective Date')
    healthfirst = load_data('Healthfirst 06.2024 Commission.xlsx', 'Member Effective Date')

    # Normalize data
    normalized_centene = normalize_data(centene, 'Writing Broker Name', 'Pay Period', 'Payment Amount', 'Centene')
    normalized_emblem = normalize_data(emblem, 'Rep Name', 'Effective Date', 'Payment', 'Emblem')
    normalized_healthfirst = normalize_data(healthfirst, 'Producer Name', 'Member Effective Date', 'Amount', 'Healthfirst')

    # Merge data
    all_commissions = merge_dataframes([normalized_centene, normalized_emblem, normalized_healthfirst])

    # Filter data for June 2024
    june_2024_commissions = filter_by_period(all_commissions, '2024-06')

    # Calculate commissions
    top_performers = calculate_commissions(june_2024_commissions)

    # Save top performers to a CSV file
    top_performers.to_csv('Top_Performers_June_2024.csv', index=False)

    # Save normalized data to a CSV file
    all_commissions.to_csv('Normalized_Commission_Data.csv', index=False)

    # Print the top 10 performers
    print("Top 10 performers in June 2024:")
    print(top_performers)

if __name__ == "__main__":
    main()

