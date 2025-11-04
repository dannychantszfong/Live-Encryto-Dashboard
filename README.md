# Live Crypto Market Dashboard

A Power BI dashboard project that visualizes real-time cryptocurrency market data. The dashboard's second page feature requires the Python web scraping script to automatically collect the latest crypto data from the internet and store timestamped snapshots for analysis.

## Overview

This is a **Power BI dashboard project** that displays cryptocurrency market data for ~1000 cryptocurrencies. The dashboard (`Live Crypto Market Overview.pbix`) relies on a Python web scraping script (`crypto_snapshots.py`) that automatically fetches the latest cryptocurrency market data from the CryptoBubbles API and stores it as CSV snapshots. The second page of the Power BI dashboard specifically requires this Python code to be running via Windows Task Scheduler to continuously update the data.

## Features

- **Power BI Dashboard**: Interactive dashboard (`Live Crypto Market Overview.pbix`) with multiple pages for cryptocurrency market analysis
- **Second Page Feature**: Requires the Python web scraping script to continuously collect data
- **Automated Web Scraping**: Python script automatically scrapes the latest cryptocurrency data from the internet
- **Real-time Data Collection**: Fetches market data for ~1000 cryptocurrencies from CryptoBubbles API
- **Timestamped Snapshots**: Saves each data collection as a CSV file with UTC timestamp
- **Standardized Data Format**: Extracts and normalizes data into a consistent format (Symbol, PriceUSD, VolumeUSD, ChangePct, SnapshotUTC)
- **Windows Task Scheduler Integration**: Designed to run automatically via Windows Task Scheduler for continuous data updates

## Project Structure

```
Live Encryto Dashboard/
├── crypto_snapshots.py          # Main Python script for data collection
├── Live Crypto Market Overview.pbix  # Power BI dashboard file
├── snapshot/                     # Directory containing CSV snapshots
│   └── snapshot_YYYYMMDD_HHMMSS.csv
└── README.md                     # This file
```

## Data Schema

Each snapshot CSV file contains the following columns:

- **Symbol**: Cryptocurrency ticker symbol (e.g., BTC, ETH)
- **PriceUSD**: Current price in USD
- **VolumeUSD**: 24-hour trading volume in USD
- **ChangePct**: 24-hour price change percentage
- **SnapshotUTC**: ISO 8601 timestamp of when the snapshot was taken (UTC)

## Prerequisites

- **Power BI Desktop** (required for viewing the dashboard)
- Python 3.6+
- Required Python packages:
  - `requests`
  - `pandas`
- **Windows Task Scheduler** (required for automated data collection for the dashboard's second page feature)

## Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd "Live Encryto Dashboard"
   ```

2. Install required Python packages:
   ```bash
   pip install requests pandas
   ```

## Usage

### Collecting Data

Run the script to fetch the latest market data and save a snapshot:

```bash
python crypto_snapshots.py
```

The script will:
1. Fetch data from the CryptoBubbles API
2. Transform the data into a standardized format
3. Save a CSV file in the `snapshot/` directory with a timestamped filename
4. Display a preview of the collected data

### Automated Collection (Required for Dashboard Second Page)

**The second page feature of the Power BI dashboard requires the Python script to run automatically via Windows Task Scheduler.**

To set up automated data collection:

1. Open Windows Task Scheduler
2. Create a new task (or basic task)
3. Configure the task:
   - **General**: Set the task to run whether user is logged on or not
   - **Triggers**: Set to run at your desired interval (e.g., every minute, every 5 minutes, or hourly)
   - **Actions**: 
     - Action: Start a program
     - Program/script: `python.exe` (or full path to your Python executable)
     - Add arguments: `"G:\Coding\data_analysis_project\Undone\Live Encryto Dashboard\crypto_snapshots.py"` (update with your actual path)
     - Start in: `G:\Coding\data_analysis_project\Undone\Live Encryto Dashboard` (update with your actual directory)
4. Save the task and test it

The script will automatically web scrape the latest cryptocurrency data from the internet and save it to the `snapshot/` directory, which the Power BI dashboard will read from.

### Viewing Data in Power BI

1. Ensure the Python script is running via Windows Task Scheduler to collect data (required for the second page feature)
2. Open `Live Crypto Market Overview.pbix` in Power BI Desktop
3. The dashboard will load the snapshot data from the `snapshot/` directory
4. Refresh the data connection in Power BI to include newly collected snapshots
5. Navigate to the second page of the dashboard to view features that rely on the automated data collection

## Configuration

The script uses the following configuration (can be modified in `crypto_snapshots.py`):

- **API URL**: `https://cryptobubbles.net/backend/data/bubbles1000.usd.json`
- **Output Directory**: `snapshot/` (relative to script location)
- **Timeout**: 30 seconds for API requests

To change the output directory, modify the `OUT_DIR` variable in the script.

## Data Source

The Python script automatically web scrapes cryptocurrency data from:
- **URL**: `https://cryptobubbles.net/backend/data/bubbles1000.usd.json`
- **Data**: Latest market data for ~1000 cryptocurrencies
- **Format**: JSON (dict or list format)
- **Method**: Automated web scraping via HTTP requests

## Notes

- Snapshot files are named using the format: `snapshot_YYYYMMDD_HHMMSS.csv`
- All timestamps are stored in UTC timezone
- The script handles missing or malformed data gracefully using pandas' `to_numeric` with error coercion
- The data extraction function is flexible and can handle various field name variations in the API response

## Contact

**Author**: Danny Chan (Tsz Fong Chan)  
**Email**: w1819419@my.westminster.ac.uk  
**LinkedIn**: [Tsz Fong Chan](https://www.linkedin.com/in/tsz-fong-chan)  
**GitHub**: [@dannychantszfong](https://github.com/dannychantszfong)

## License

This project is provided as-is for educational and personal use.

