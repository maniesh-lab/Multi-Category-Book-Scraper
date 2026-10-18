def clean_data(df):

    df = df.dropna()
    df = df.drop_duplicates()
    df = df.reset_index(drop=True)
    df["Price"] = df["Price"].str.replace("£","", regex=False)
    df["Price"] = df["Price"].astype(float)
    
    return df