import yfinance as yf
import pandas as pd
import sqlite3

# ----------------------------
# STEP 1: STOCK LIST
# ----------------------------
stocks = ["AAPL", "MSFT", "GOOGL"]

all_data = []

# ----------------------------
# STEP 2: FETCH + CLEAN DATA
# ----------------------------
for stock in stocks:
    print(f"Fetching {stock}...")

    df = yf.Ticker(stock).history(period="1mo")

    # Clean missing values
    df = df.dropna()

    # Reset index (Date becomes column)
    df = df.reset_index()

    # Add stock name column
    df["Stock"] = stock

    all_data.append(df)

# ----------------------------
# STEP 3: COMBINE DATA
# ----------------------------
final_df = pd.concat(all_data, ignore_index=True)

print("\nData preview:")
print(final_df.head())

# ----------------------------
# STEP 4: SAVE TO SQLITE (LEVEL 2)
# ----------------------------
conn = sqlite3.connect("stocks.db")

final_df.to_sql(
    "ohlcv_data",   # table name
    conn,
    if_exists="replace",  # overwrite old data each run
    index=False
)

print("\n✅ Data successfully saved to SQLite database (stocks.db)")

