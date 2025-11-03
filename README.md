# Sentiment Analysis App

A web application that displays the stock market sentiment from Alpha Vantage and the Fear & Greed Index from alternative.me.

## Features

- Displays the current Fear & Greed Index.
- Displays the latest stock market news and their sentiment.

## Installation

1. Clone the repository:
   ```bash
   git clone 
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Create a `.env` file in the root directory and add your Alpha Vantage API key:
   ```
   ALPHA_VANTAGE_API_KEY=YOUR_API_KEY
   ```
2. Run the backend server:
   ```bash
   python app.py
   ```
3. View in your web browser.

## Configuration

- `ALPHA_VANTAGE_API_KEY`: Your API key for Alpha Vantage.
