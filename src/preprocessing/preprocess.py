import pandas as pd
import os

def load_data():
    """
    Load the raw dataset from the 'data/raw/' directory.
    Returns:
        pd.DataFrame: The loaded dataset.
    """
    file_path = 'data/raw/Sleep_health_and_lifestyle_dataset.csv'
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Raw dataset not found at {file_path}. Ensure the file exists.")
    
    print("Loading data...")
    data = pd.read_csv(file_path)
    print("Data loaded successfully!")
    print(f"Initial Data Shape: {data.shape}")
    return data


def clean_data():
    """
    Clean the dataset by removing duplicates and rows with missing values.
    Saves the cleaned dataset to 'data/processed/'.
    """
    # Load the data
    data = load_data()

    # Display missing values
    print("Checking for missing values...")
    print(data.isnull().sum())

    # Remove duplicate rows
    print("Removing duplicate rows...")
    data = data.drop_duplicates()

    # Drop rows with missing values
    print("Dropping rows with missing values...")
    data = data.dropna()

    # Ensure the processed folder exists
    os.makedirs('data/processed', exist_ok=True)

    # Save cleaned data
    processed_file_path = 'data/processed/cleaned_data.csv'
    data.to_csv(processed_file_path, index=False)
    print(f"Data cleaned and saved to {processed_file_path}")


if __name__ == "__main__":
    print("Starting data preprocessing...")
    try:
        clean_data()
        print("Data preprocessing completed successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
