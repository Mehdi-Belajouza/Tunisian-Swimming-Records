import requests
from bs4 import BeautifulSoup
import json
import csv
from typing import Dict, List
import re
import os

def normalize_event_name(event: str) -> str:
    """Normalize event name to ensure consistent formatting across all sources"""
    event = event.replace('×', 'x').replace('Ã—', 'x').replace('â€"', 'x')
    event = re.sub(r'\s+', ' ', event)
    event = re.sub(r'\s*x\s*', 'x', event)
    event = re.sub(r'(\d+)\s*m\s', r'\1m ', event)
    event = re.sub(r'\s+', ' ', event).strip()
    return event

def scrape_country_records(url: str, country: str) -> Dict:
    """
    Scrapes swimming records from Wikipedia for a specific Arab country
    """
    print(f"\nFetching {country.upper()} records from Wikipedia...")
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        all_records = {
            'long_course': {
                'men': [],
                'women': [],
                'mixed_relay': []
            },
            'short_course': {
                'men': [],
                'women': []
            }
        }
        
        # Find all tables in the page
        tables = soup.find_all('table', class_='wikitable')
        
        print(f"Found {len(tables)} tables for {country}")
        
        for table in tables:
            # Get the section heading to determine what type of records
            heading = table.find_previous(['h3', 'h2'])
            if not heading:
                continue
                
            section_text = heading.get_text().strip()
            
            # Determine course type and category
            course_type = None
            category = None
            
            # Check if we're in Long Course or Short Course section
            h2_heading = table.find_previous('h2')
            if h2_heading:
                h2_text = h2_heading.get_text().strip()
                if 'Long course' in h2_text or 'Long Course' in h2_text:
                    course_type = 'long_course'
                elif 'Short course' in h2_text or 'Short Course' in h2_text:
                    course_type = 'short_course'
            
            # Determine category (Men/Women/Mixed)
            if 'Men' in section_text and 'Women' not in section_text:
                category = 'men'
            elif 'Women' in section_text:
                category = 'women'
            elif 'Mixed' in section_text:
                category = 'mixed_relay'
            
            if not course_type or not category:
                continue
            
            # Skip if mixed_relay in short_course (doesn't exist)
            if course_type == 'short_course' and category == 'mixed_relay':
                continue
                
            # Extract table rows
            rows = table.find_all('tr')
            
            for row in rows[1:]:  # Skip header row
                cols = row.find_all(['td', 'th'])
                if len(cols) < 4:  # Skip rows with insufficient data
                    continue
                
                try:
                    event = cols[0].get_text().strip()
                    event = normalize_event_name(event)
                    time = cols[1].get_text().strip()
                    record_type = cols[2].get_text().strip() if len(cols) > 2 else ''
                    
                    # Extract swimmer name
                    swimmer_cell = cols[3] if len(cols) > 3 else None
                    if swimmer_cell:
                        swimmer_text = swimmer_cell.get_text(separator='|').strip()
                        parts = [part.strip() for part in swimmer_text.split('|') if part.strip()]
                        swimmer = ', '.join(parts)
                    else:
                        swimmer = ''
                    
                    club = cols[4].get_text().strip() if len(cols) > 4 else country
                    date = cols[5].get_text().strip() if len(cols) > 5 else ''
                    meet = cols[6].get_text().strip() if len(cols) > 6 else ''
                    location = cols[7].get_text().strip() if len(cols) > 7 else ''
                    
                    # Clean up placeholders
                    if club in ['-', '–', '']: club = country
                    if date in ['-', '–']: date = ''
                    if meet in ['-', '–']: meet = ''
                    if location in ['-', '–']: location = ''
                    
                    # Skip empty events or legend rows
                    if not event or 'Legend' in event or event == 'Event' or not time:
                        continue
                    
                    record = {
                        'event': event,
                        'time': time,
                        'record_type': record_type,
                        'swimmer': swimmer,
                        'club': club,
                        'country': country,
                        'date': date,
                        'meet': meet,
                        'location': location,
                        'course': course_type.replace('_', ' ').title(),
                        'category': category.replace('_', ' ').title()
                    }
                    
                    all_records[course_type][category].append(record)
                    
                except Exception as e:
                    print(f"Error parsing row in {country}: {e}")
                    continue
        
        return all_records
        
    except Exception as e:
        print(f"Error fetching {country} records: {e}")
        return None

def save_to_json(records: Dict, filename: str):
    """Save records to JSON file"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(records, f, indent=2, ensure_ascii=False)
    print(f"✓ Saved {filename}")

def display_summary(records: Dict, country: str):
    """Display scraping summary"""
    if not records:
        print(f"  ✗ No records found for {country}")
        return
        
    total_records = 0
    for course_type, categories in records.items():
        for category, record_list in categories.items():
            total_records += len(record_list)
    
    print(f"  ✓ {country}: {total_records} records")

def main():
    print("=" * 70)
    print("ARAB COUNTRIES SWIMMING RECORDS SCRAPER")
    print("=" * 70)
    
    # Arab countries with Wikipedia swimming records pages
    arab_countries = {
        'Tunisia': 'https://en.wikipedia.org/wiki/List_of_Tunisian_records_in_swimming',
        'Egypt': 'https://en.wikipedia.org/wiki/List_of_Egyptian_records_in_swimming',
        'Morocco': 'https://en.wikipedia.org/wiki/List_of_Moroccan_records_in_swimming',
        'Algeria': 'https://en.wikipedia.org/wiki/List_of_Algerian_records_in_swimming',
        'UAE': 'https://en.wikipedia.org/wiki/List_of_United_Arab_Emirates_records_in_swimming',
        'Saudi Arabia': 'https://en.wikipedia.org/wiki/List_of_Saudi_Arabian_records_in_swimming',
        'Qatar': 'https://en.wikipedia.org/wiki/List_of_Qatari_records_in_swimming',
        'Kuwait': 'https://en.wikipedia.org/wiki/List_of_Kuwaiti_records_in_swimming',
        'Bahrain': 'https://en.wikipedia.org/wiki/List_of_Bahraini_records_in_swimming',
        'Lebanon': 'https://en.wikipedia.org/wiki/List_of_Lebanese_records_in_swimming',
        'Oman': 'https://en.wikipedia.org/wiki/List_of_Omani_records_in_swimming',
        'Jordan': 'https://en.wikipedia.org/wiki/List_of_Jordanian_records_in_swimming',
        'Iraq': 'https://en.wikipedia.org/wiki/List_of_Iraqi_records_in_swimming',
        'Syria': 'https://en.wikipedia.org/wiki/List_of_Syrian_records_in_swimming',
        'Palestine': 'https://en.wikipedia.org/wiki/List_of_Palestinian_records_in_swimming',
    }
    
    all_countries_data = {}
    successful_countries = []
    failed_countries = []
    
    print("\nScraping records from Arab countries...")
    print("-" * 70)
    
    # Create data directory if it doesn't exist
    os.makedirs('../data/arab_countries', exist_ok=True)
    
    # Scrape each country
    for country, url in arab_countries.items():
        records = scrape_country_records(url, country)
        if records and any(len(records[ct][cat]) > 0 for ct in records for cat in records[ct]):
            all_countries_data[country] = records
            display_summary(records, country)
            save_to_json(records, f'../data/arab_countries/{country.lower().replace(" ", "_")}_swimming_records.json')
            successful_countries.append(country)
        else:
            failed_countries.append(country)
            print(f"  ✗ {country}: No data or page not found")
    
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"✓ Successfully scraped: {len(successful_countries)} countries")
    print(f"  {', '.join(successful_countries)}")
    
    if failed_countries:
        print(f"\n✗ Failed to scrape: {len(failed_countries)} countries")
        print(f"  {', '.join(failed_countries)}")
        print("\n  Note: Some countries may not have Wikipedia pages for swimming records.")
    
    # Save combined data
    if all_countries_data:
        save_to_json(all_countries_data, '../data/arab_countries/all_arab_countries_records.json')
        print(f"\n✓ Combined data saved to: data/arab_countries/all_arab_countries_records.json")
    
    print("\n" + "=" * 70)
    print("Next step: Run 'aggregate_arab_records.py' to find best Arab records!")
    print("=" * 70)

if __name__ == "__main__":
    main()
