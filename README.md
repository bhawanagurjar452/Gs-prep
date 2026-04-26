📊  Stock Data Pipeline



🚀 Project Overview



This project builds a simple \*\*ETL (Extract, Transform, Load) pipeline\*\* using Python.



It fetches stock market data, cleans it, performs basic analysis, and stores it in a SQLite database.



\---



📦 Features



\* Fetch OHLCV stock data (Open, High, Low, Close, Volume)

\* Clean missing values using pandas

\* Combine multiple stocks into one dataset

\* Calculate:



&#x20; \* Daily Returns

&#x20; \* 20-day Moving Average (MA20)

\* Store processed data in SQLite database



\---



🧠 ETL Pipeline Explained

1\. Extract



\* Data is fetched from Yahoo Finance using `yfinance`

\* Stocks used:



&#x20; \* AAPL

&#x20; \* MSFT

&#x20; \* GOOGL



2\. Transform



\* Remove missing values

\* Reset index (Date column)

\* Add stock identifier

\* Calculate:



&#x20; \* Returns = percentage change in price

&#x20; \* MA20 = 20-day moving average



3\. Load



\* Data is saved into a SQLite database:



&#x20; \* File: `stocks.db`

&#x20; \* Table: `ohlcv\_data`



\---



⚙️ Tech Stack



\* Python

\* pandas

\* yfinance

\* SQLite



\---



▶️ How to Run the Project



1\. Clone the repository



```

git clone https://github.com/YOUR\_USERNAME/gs-prep.git

cd gs-prep

```



2\. Create virtual environment



```

python -m venv venv

source venv/Scripts/activate   # Windows (Git Bash)

```



3\. Install dependencies



```

pip install -r requirements.txt

```



4\. Run the pipeline



```

python src/pipeline.py

```



\---



📂 Output



After running the script:



\* SQLite database file:



&#x20; ```

&#x20; stocks.db

&#x20; ```



\* Table:



&#x20; ```

&#x20; ohlcv\_data

&#x20; ```



Contains:



\* Date

\* Open, High, Low, Close

\* Volume

\* Stock

\* Returns

\* MA20



\---



&#x20;📈 Future Improvements



\* Add visualization (charts)

\* Automate daily data updates

\* Upgrade to PostgreSQL

\* Build dashboard (Power BI)



\---



👨‍💻 Author



Bhawna Gurjar



