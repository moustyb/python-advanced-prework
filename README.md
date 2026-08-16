# Country Explorer CLI

This project is a command-line interface (CLI) tool built for the **Code the Dream - Python Advanced Pre-Work**. It fetches live, real-world data about countries and formats it cleanly for the user.

## Features
- **API Integration:** Connects to the [countries.dev](https://countries.dev) REST API.
- **Multiple Interaction Modes:** Users can search for a specific country by name or filter a list of countries by region.
- **Robust Error Handling:** gracefully handles network connection errors, API 404 Not Found status codes, and missing data fields without crashing.
- **Modular Code:** Logic is cleanly separated into single-responsibility functions (fetching, transforming, and displaying).

## Prerequisites
You will need Python 3 installed on your computer, along with the `requests` library.

## Installation & Setup
1. Clone this repository to your local machine.
2. Navigate to the project folder in your terminal.
3. Install the required dependencies by running:
   ```bash
   pip install -r requirements.txt
