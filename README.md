# 📊 Tokopedia Price Tracker

## 🌟 Project Overview

Tokopedia Price Tracker is a Django-based web application that allows users to track and monitor product prices from Tokopedia. With this tool, you can easily:
- Add product links for tracking
- Monitor price changes
- Get insights into price fluctuations

## 🚀 Features

- **Price Tracking**: Monitor prices of products from Tokopedia
- **CRUD Functionality**: 
  - Create new product links
  - Read product details
  - Update existing links
  - Delete tracked items
- **Price Change Insights**:
  - Track current and old prices
  - Calculate price differences
  - Highlight discounted items
- **Responsive UI**: Modern, mobile-friendly design
- **User-Friendly**: Simple and intuitive interface

## 🛠 Technologies Used

- **Backend**: Django
- **Frontend**: 
  - Bootstrap 5
  - Bootstrap Icons
- **Database**: SQLite (default)
- **Dependencies**: 
  - requests (for web scraping)
  - crispy-forms

## 📋 Prerequisites

- Python 3.8+
- pip
- virtualenv (recommended)

## 🔧 Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/tokopedia-price-tracker.git
cd tokopedia-price-tracker
```

2. Create a new virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Start the development server:
```bash
python manage.py runserver
```


## 🌈 Usage

Open the application in your browser
Click "Add New Link" to start tracking a Tokopedia product
Paste the product URL
View and manage your tracked products


## 🔍 How It Works
The application scrapes basic product information from the provided Tokopedia link
Tracks price changes over time
Provides a dashboard to view all tracked products
 
## 🚧 Roadmap
[ ] Implement price history charts
[ ] Add email notifications for price drops
[ ] Support multiple e-commerce platforms
[ ] Improve web scraping reliability

