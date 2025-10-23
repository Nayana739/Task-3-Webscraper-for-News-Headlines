# Web Scraper for News Headlines

Automate the collection of top news headlines from a public website and save them to a `.txt` file using Python.

## Requirements
* **Python 3.11**
* [`requests`](https://pypi.org/project/requests/) – for fetching HTML content  
* [`beautifulsoup4`](https://pypi.org/project/beautifulsoup4/) – for parsing and extracting headlines  
* **VS Code** – for development and interpreter management  
* **Git & GitHub** – for version control and repo presentation

## Features
* Scrapes headlines from `<h1>`, `<h2>`, and `<h3>` tags  
* Filters out short or empty titles  
* Saves results to `top_headlines.txt` with numbered formatting  
* Successfully extracted **58 headlines** from BBC News

##  How to Run

### 1. Install dependencies
```bash
pip install requests beautifulsoup4
```

### 2. Run the script
```bash
python news_scraper.py
```

> If using a specific interpreter:
```powershell
& "C:\Users\Others\AppData\Local\Programs\Python\Python311\python.exe" "webscraper.py"
```

## Output
* A file named `top_headlines.txt` containing the scraped headlines, one per line.

## Troubleshooting Highlights
* Resolved `ModuleNotFoundError` by switching from  Python 3.12 to system Python 3.11  
* Installed missing packages and verified interpreter paths  
* Used PowerShell to run the script with the correct interpreter  

