import pandas as pd
import psycopg2

# Load the dataset
df = pd.read_csv("Data/Sample-Superstore.csv", parse_dates=["Order Date", "Ship Date"])

# Rename columns to match SQL table (remove spaces and special characters)
df.columns = df.columns.str.lower().str.replace(" ", "_").str.replace("-", "_")

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="sales_db",
    user="your_username",  # Change this to your PostgreSQL username
    password="your_password",  # Change this to your PostgreSQL password
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# Insert Data
for _, row in df.iterrows():
    cur.execute("""
        INSERT INTO sales (
            order_id, order_date, ship_date, ship_mode, customer_id, customer_name, segment, 
            country, city, state, postal_code, region, product_id, category, sub_category, 
            product_name, sales, quantity, discount, profit
        ) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    """, (
        row["order_id"], row["order_date"], row["ship_date"], row["ship_mode"],
        row["customer_id"], row["customer_name"], row["segment"], row["country"],
        row["city"], row["state"], row["postal_code"], row["region"], row["product_id"],
        row["category"], row["sub_category"], row["product_name"], row["sales"],
        row["quantity"], row["discount"], row["profit"]
    ))

# Commit changes and close connection
conn.commit()
cur.close()
conn.close()

print("Data Loaded Successfully!")
