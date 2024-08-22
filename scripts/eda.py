import pandas as pd

def load_data(file_path):
    """Load the dataset from the specified CSV file."""
    data = pd.read_csv(file_path)
    return data

def summarize_data(data):
    """Generate summary statistics for the dataset."""
    summary_stats = data.describe()
    missing_values = data.isnull().sum()
    return summary_stats, missing_values

def check_negative_values(data):
    """Check for negative values in solar irradiance columns."""
    negative_values = {
        "GHI": (data['GHI'] < 0).sum(),
        "DNI": (data['DNI'] < 0).sum(),
        "DHI": (data['DHI'] < 0).sum(),
    }
    return negative_values

def clean_data(data):
    """Clean the dataset by handling negative values and dropping the Comments column."""
    # Replace negative values in GHI, DNI, DHI with 0
    data['GHI'] = data['GHI'].apply(lambda x: max(x, 0))
    data['DNI'] = data['DNI'].apply(lambda x: max(x, 0))
    data['DHI'] = data['DHI'].apply(lambda x: max(x, 0))
    
    # Drop the Comments column
    data = data.drop(columns=['Comments'])
    
    return data

def save_cleaned_data(data, output_path):
    """Save the cleaned dataset to the specified CSV file."""
    data.to_csv(output_path, index=False)

if __name__ == "__main__":
    # Define the file paths
    file_path = '/home/kali/Downloads/data/benin-malanville.csv'
    output_path = '/home/kali/Downloads/data/benin-malanville-cleaned.csv'
    
    # Load the data
    data = load_data(file_path)
    
    # Generate summary statistics
    summary_stats, missing_values = summarize_data(data)
    print("Summary Statistics:\n", summary_stats)
    print("\nMissing Values:\n", missing_values)
    
    # Check for negative values
    negative_values = check_negative_values(data)
    print("\nNegative Values:\n", negative_values)
    
    # Clean the data
    cleaned_data = clean_data(data)
    
    # Save the cleaned data
    save_cleaned_data(cleaned_data, output_path)
