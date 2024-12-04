def clean_data():
    import os
    print("Loading data...")
    data = pd.read_csv('data/raw/Sleep_health_and_lifestyle_dataset.csv')
    print("Data loaded successfully!")

    # Display basic information
    print("Initial Data Shape:", data.shape)
    print("Checking for missing values...")
    print(data.isnull().sum())

    # Remove duplicate rows
    print("Removing duplicates...")
    data = data.drop_duplicates()

    # Drop rows with missing values
    print("Dropping missing values...")
    data = data.dropna()

    # Ensure the processed folder exists
    os.makedirs('data/processed', exist_ok=True)

    # Save cleaned data
    print("Saving cleaned data...")
    data.to_csv('data/processed/cleaned_data.csv', index=False)
    print("Data cleaned and saved to data/processed/cleaned_data.csv")

