import pandas as pd

def load_data():
    # Load the raw dataset
    data = pd.read_csv('data/raw/Sleep_health_and_lifestyle_dataset.csv')
    print("Data loaded successfully!")
    return data

def clean_data():
    # Load the data
    data = pd.read_csv('data/raw/Sleep_health_and_lifestyle_dataset.csv')
    
    # Display basic information
    print("Initial Data Shape:", data.shape)
    print("Checking for missing values...")
    print(data.isnull().sum())

    # Remove duplicate rows
    data = data.drop_duplicates()
    
    # Drop rows with missing values
    data = data.dropna()
    
    # Save cleaned data
    data.to_csv('data/processed/cleaned_data.csv', index=False)
    print("Data cleaned and saved to data/processed/cleaned_data.csv")

