import requests
import sys

def fetch_api_data(endpoint, query_params):
    """
    Fetches data from the countries.dev API.
    Wraps the API call in a try/except block to handle connection errors gracefully.
    """
    base_url = "https://countries.dev"
    url = f"{base_url}{endpoint}"
    
    try:
        response = requests.get(url, params=query_params)
        
        # Handle specifically if country/region is not found
        if response.status_code == 404:
            print("\n[!] No results found. Please check your spelling and try again.")
            return None
            
        # Handle other HTTP errors
        response.raise_for_status()
        return response.json()
        
    except requests.exceptions.RequestException:
        print("\n[!] Connection Error: Unable to connect to the API. Please check your internet connection.")
        return None

def transform_country_data(raw_data):
    """
    Parses the raw JSON response into a list of dictionaries.
    Uses .get() to handle missing keys safely without crashing.
    """
    # API might return a single dictionary or a list of dictionaries. 
    # We ensure it's always a list for consistent processing.
    if isinstance(raw_data, dict):
        raw_data = [raw_data]
        
    clean_countries = []
    
    for country in raw_data:
        # Using .get() ensures the program doesn't crash if a field is missing (like Antarctica having no capital)
        name = country.get("name", "Unknown Country")
        capital = country.get("capital", "No Capital")
        population = country.get("population", 0)
        
        clean_countries.append({
            "name": name,
            "capital": capital,
            "population": population
        })
        
    return clean_countries

def display_results(countries):
    """
    Displays the extracted data in a clean, readable format.
    """
    if not countries:
        return
        
    print("\n--- Search Results ---")
    for c in countries:
        print(f"Country    : {c['name']}")
        print(f"Capital    : {c['capital']}")
        # Format the population with commas for better readability
        print(f"Population : {c['population']:,}")
        print("-" * 22)

def main():
    """
    Main CLI controller. Provides multiple interaction modes via a menu.
    """
    while True:
        print("\n=== Country Explorer CLI ===")
        print("1. Search for a specific country by name")
        print("2. Filter countries by region (e.g., Europe, Asia)")
        print("3. Exit program")
        
        choice = input("\nSelect an option (1-3): ").strip()
        
        if choice == "1":
            country_name = input("Enter country name: ").strip()
            if not country_name:
                print("\n[!] Input cannot be empty.")
                continue
                
            # Passing parameters as arguments to exceed expectations
            params = {"fields": "name,capital,population"}
            raw_data = fetch_api_data(f"/name/{country_name}", params)
            
            if raw_data:
                processed_data = transform_country_data(raw_data)
                display_results(processed_data)
                
        elif choice == "2":
            region_name = input("Enter region name: ").strip()
            if not region_name:
                print("\n[!] Input cannot be empty.")
                continue
                
            params = {"fields": "name,capital,population"}
            raw_data = fetch_api_data(f"/region/{region_name}", params)
            
            if raw_data:
                processed_data = transform_country_data(raw_data)
                display_results(processed_data)
                
        elif choice == "3":
            print("\nExiting Country Explorer. Have a great day!")
            sys.exit()
            
        else:
            print("\n[!] Invalid selection. Please type 1, 2, or 3.")

if __name__ == "__main__":
    main()
