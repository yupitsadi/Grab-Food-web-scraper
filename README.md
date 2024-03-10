# Project Title.
## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Welcome to the Grab Web Scraper project! This Python-based web scraping tool is designed to extract and analyze data from the GrabFood website. The scraper collects information about restaurants, recommended merchants, and various details related to the GrabFood platform.

## Features

- **Web Scraping:** Extracts data from the GrabFood website, focusing on restaurant information and recommended merchants.
- **Data Processing:** Parses the extracted data and organizes it into structured formats.
- **API Requests:** Fetches detailed information about specific merchants using Grab's API.

## Getting Started

To get started with this project, follow the installation instructions and explore the various features available.

## How It Works

1. **Web Scraping:** The initial script (1_webScraper.py) uses BeautifulSoup to scrape HTML content from the GrabFood website.
2. **Data Processing:** The extracted data is then processed and organized, and relevant information is stored in a JSON file.
3. **API Requests:** The ResListFetch script (2_RestListFetch.py) uses the collected IDs to make API requests and fetch detailed information about specific merchants.
4. **Data Combining:** The ListMaking script (3_listMaking.py) combines the collected data into a structured format.
5. **Response Grab:** The final script (4_responseGrab.py) uses the collected IDs to fetch responses and extract specific details about merchants.

## Features

1. **Web Scraping:** Utilize BeautifulSoup for efficient extraction of data from the GrabFood website, focusing on restaurants and recommended merchants.

2. **Data Processing:** Process and organize the extracted data into a structured format for further analysis and presentation.

3. **API Requests:** Make API requests to Grab's servers using the collected merchant IDs to fetch detailed information about specific merchants.

4. **Data Combination:** Combine the collected data into a cohesive and structured format using ListMaking script for comprehensive analysis.

5. **Response Grab:** Fetch responses using the collected IDs, extracting specific details about merchants for a deeper understanding.

6. **Ease of Use:** Designed to be user-friendly, allowing seamless execution of scripts to gather and process data without unnecessary complexity.

7. **Customizable:** Easily adapt the scripts to accommodate changes in the GrabFood website structure or modify them for specific use cases.

8. **Contributions Welcome:** We encourage contributions from the community to enhance and improve the functionality of the web scraper.

9. **Documentation:** Detailed documentation to guide users on installation, usage, and contributing to the project.

10. **Open Source:** Released under an open-source license, fostering collaboration and transparency within the developer community.

11. **Scalability:** Designed with scalability in mind to handle a large volume of data efficiently.

12. **Modular Architecture:** Scripts are organized in a modular manner, making it easy to understand, extend, or modify specific functionalities.

### Prerequisites

Before getting started with the GrabFood Web Scraper project, make sure you have the following prerequisites installed:

1. **Python:** Ensure you have Python installed on your machine. You can download and install it from [python.org](https://www.python.org/).

2. **Dependencies:** Install the required Python libraries using the following command:

   ```bash
   pip install -r requirements.txt

### Installation

## Installation

Follow these steps to set up and run the GrabFood Web Scraper:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/grabfood-web-scraper.git

2. **Change Directory**
    ```bash
    cd grabfood-web-scraper

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt

4. **Make the script executable**
   ```bash
   chmod +x run_scripts.sh 

5. **Execute the script**
   ```bash
   ./run_scripts.sh   
