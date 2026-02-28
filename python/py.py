import pandas as pd

# Lire le datase
df = pd.read_csv("python/amazon_raw.csv")

#affiicher les 5 premiere lignnes 
print(df.head())

#afficher les colones 
print(df.columns)

# Colonnes utiles pour le suivi des ventes
columns_to_keep = [  # columns_to_keep tableau que l'on declare
     "product_id",
     "user_name",
     "user_id",
    "product_name",
    "category",
    "discounted_price",
    "actual_price",
    "discount_percentage",
    "rating",
    "rating_count"
]
print(" le filtrage :")
df = df[columns_to_keep]
print(df)

# Nettoyage des prix

df["discounted_price"] = (
    df["discounted_price"].astype("string")
)

df["discounted_price"] = (
    df["discounted_price"]
    .str.replace("₹", "", regex=False)
    .str.replace(",", "", regex=False)
    .astype(float)
)


df["actual_price"] = (
    df["actual_price"].astype("string")
)

df["actual_price"] = (
    df["actual_price"]
    .str.replace("₹", "", regex=False)
    .str.replace(",", "", regex=False)
    .astype(float)
)