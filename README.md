Jumia Product Price Scraper*

A Python web scraping project that collects product information and prices from Jumia Kenya and organizes the data into a structured format for analysis.

The project uses Requests and BeautifulSoup to retrieve and parse web page content, then saves the extracted product data for further analysis.

*Project Overview*

The goal of this project is to practice real-world web scraping and data processing using Python.

The scraper extracts product information such as:

Product name
Product price
Product URL
Product information available on the page

The collected data can then be stored in CSV or JSON format for analysis.

*Technologies Used*
Python 3
Requests – sends HTTP requests to retrieve web pages
BeautifulSoup – parses HTML and extracts data
CSV – stores scraped product data
JSON – stores structured data
Pandas – useful for data analysis
Git & GitHub – version control and project management

*Project outline*
jumia_scrape/
│
├── jumia_scrape.py       # Main web scraping script
├── jumia_items.csv       # Scraped product data
├── requirements.txt      # Python dependencies
├── .gitignore            # Files excluded from Git
└── README.md             # Project documentation

*How It Works*

The scraper follows these basic steps:

Jumia Kenya
     ↓
Send HTTP Request
     ↓
Receive HTML
     ↓
Parse HTML with BeautifulSoup
     ↓
Find Product Information
     ↓
Extract Prices & Product Details
     ↓
Store Data
     ↓
CSV / JSON
▶️ Installation
1. Clone the repository
git clone https://github.com/patrickmnj/price_practice.git
2. Navigate to the project directory
cd price_practice
3. Create a virtual environment
python -m venv .venv
4. Activate the virtual environment

Windows:

.venv\Scripts\activate

Git Bash:

source .venv/Scripts/activate
5. Install dependencies
pip install -r requirements.txt
▶️ Running the Scraper

Run the Python script:

python jumia_scrape.py

The script retrieves the available product information and saves the results into a CSV file.

📊 Example Output

The resulting dataset can contain information similar to:

Product	Price	URL
Smartphone	KSh 15,999	Product URL
Laptop	KSh 45,000	Product URL
Headphones	KSh 2,500	Product URL

The exact products and prices may change because the website's content changes over time.

 Currency Conversion

The project can also be extended to convert scraped prices into another currency using an exchange-rate API or any other API ,i used *https://api.frankfurter.dev/v2/rates/*
[.

For example:

KES → USD

This makes the project useful not only for scraping but also for data transformation and analysis.

 *What I Learned*

This project helped me practice:

Making HTTP requests with requests
Parsing HTML with BeautifulSoup
Finding HTML elements
Extracting product information
Working with prices and strings
Handling missing data
Writing data to CSV
Working with JSON
Using virtual environments
Managing Python dependencies
Using Git and GitHub
Debugging web scraping problems

 *Challenges*

One of the main challenges was identifying the correct HTML elements containing product information.

Some of the products have the actual prices and discounts 

This project helped me understand that web scraping requires both Python knowledge and the ability to inspect and understand HTML structure.

🔮 Future Improvements

Possible improvements include:

Scrape more product categories

Extract product ratings

Extract number of reviews

Extract product discounts

Add pagination

Add automatic currency conversion and current rate

Increase number currency

Store data in a database

Use Pandas for data analysis

Create price comparison charts

⚠️ Disclaimer

This is an educational project.

👨‍💻 Author

Patrick Njuguna

Python learner | Web Scraping | Data Analytics

This project is part of my journey toward building practical Python and Data Analytics projects.
