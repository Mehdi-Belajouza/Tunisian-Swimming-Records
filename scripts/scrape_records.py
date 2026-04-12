import requests
from bs4 import BeautifulSoup
import json
import csv
from typing import Dict, List
import re
import os

def normalize_event_name(event: str) -> str:
    """Normalize event name to ensure consistent formatting across all sources"""
    # Replace multiplication signs with 'x'
    event = event.replace('×', 'x').replace('Ã—', 'x').replace('â€"', 'x')
    # Remove extra spaces
    event = re.sub(r'\s+', ' ', event)
    # Standardize spacing around 'x'
    event = re.sub(r'\s*x\s*', 'x', event)
    # Standardize meter notation (100 m -> 100m)
    event = re.sub(r'(\d+)\s*m\s', r'\1m ', event)
    # Clean up
    event = re.sub(r'\s+', ' ', event).strip()
    return event

def scrape_swimming_records(url: str, region: str) -> Dict:
    """
    Scrapes swimming records from Wikipedia
    Args:
        url: Wikipedia URL for the records
        region: 'tunisia', 'arab', 'africa', or 'world'
    """
    print(f"\nFetching {region.upper()} records from Wikipedia...")
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers)
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
        
        print(f"Found {len(tables)} tables")
        
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
                
                # Extract data from columns
                try:
                    event = cols[0].get_text().strip()
                    # Normalize event name for consistency
                    event = normalize_event_name(event)
                    time = cols[1].get_text().strip()
                    
                    # For world records, structure might be different
                    if region == 'world':
                        # World records typically have: Event, Time, Name, Nation, Date, Meet, Location
                        record_type = ''
                        # Extract swimmer name directly from col[2]
                        swimmer = cols[2].get_text(separator='|').strip() if len(cols) > 2 else ''
                        # Split by | and join with commas for relays
                        if swimmer:
                            parts = [part.strip() for part in swimmer.split('|') if part.strip()]
                            swimmer = ', '.join(parts)
                        
                        nation = cols[3].get_text().strip() if len(cols) > 3 else ''
                        date = cols[4].get_text().strip() if len(cols) > 4 else ''
                        meet = cols[5].get_text().strip() if len(cols) > 5 else ''
                        location = cols[6].get_text().strip() if len(cols) > 6 else ''
                        club = nation
                    else:
                        record_type = cols[2].get_text().strip() if len(cols) > 2 else ''
                        swimmer_cell = cols[3] if len(cols) > 3 else None
                        club = cols[4].get_text().strip() if len(cols) > 4 else ''
                        date = cols[5].get_text().strip() if len(cols) > 5 else ''
                        meet = cols[6].get_text().strip() if len(cols) > 6 else ''
                        location = cols[7].get_text().strip() if len(cols) > 7 else ''
                        
                        # Fix swimmer names - add proper spacing for relays
                        if swimmer_cell:
                            # Get all text and clean it up
                            swimmer_text = swimmer_cell.get_text(separator='|').strip()
                            # Split by | and clean each part
                            parts = [part.strip() for part in swimmer_text.split('|') if part.strip()]
                            swimmer = ', '.join(parts)
                        else:
                            swimmer = ''
                    
                    # Clean up placeholders
                    if club == '-' or club == '–': club = ''
                    if date == '-' or date == '–': date = ''
                    if meet == '-' or meet == '–': meet = ''
                    if location == '-' or location == '–': location = ''
                    
                    # Skip empty events or legend rows
                    if not event or 'Legend' in event or event == 'Event' or not time:
                        continue
                    
                    record = {
                        'event': event,
                        'time': time,
                        'record_type': record_type,
                        'swimmer': swimmer,
                        'club': club,
                        'date': date,
                        'meet': meet,
                        'location': location,
                        'course': course_type.replace('_', ' ').title(),
                        'category': category.replace('_', ' ').title()
                    }
                    
                    all_records[course_type][category].append(record)
                    
                except Exception as e:
                    print(f"Error parsing row: {e}")
                    continue
        
        return all_records
        
    except Exception as e:
        print(f"Error fetching {region} records: {e}")
        return None

def save_to_json(records: Dict, filename: str):
    """Save records to JSON file"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(records, f, indent=2, ensure_ascii=False)
    print(f"Data saved to {filename}")

def save_to_csv(records: Dict, filename: str):
    """Save records to CSV file"""
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Course', 'Category', 'Event', 'Time', 'Record Type', 
                        'Swimmer', 'Club/Nation', 'Date', 'Meet', 'Location'])
        
        for course_type, categories in records.items():
            for category, record_list in categories.items():
                for record in record_list:
                    writer.writerow([
                        record['course'],
                        record['category'],
                        record['event'],
                        record['time'],
                        record['record_type'],
                        record['swimmer'],
                        record['club'],
                        record['date'],
                        record['meet'],
                        record['location']
                    ])
    print(f"Data saved to {filename}")

def display_summary(records: Dict, region: str):
    """Display scraping summary"""
    print(f"\n{region.upper()} RECORDS SUMMARY")
    print("=" * 50)
    
    total_records = 0
    for course_type, categories in records.items():
        print(f"\n{course_type.replace('_', ' ').title()}:")
        for category, record_list in categories.items():
            count = len(record_list)
            total_records += count
            print(f"  {category.replace('_', ' ').title()}: {count} records")
    
    print(f"\nTotal Records: {total_records}")
    print("=" * 50)

def main():
    print("=" * 60)
    print("SWIMMING RECORDS COMPREHENSIVE SCRAPER")
    print("=" * 60)
    
    # Define all the sources
    sources = {
        'tunisia': 'https://en.wikipedia.org/wiki/List_of_Tunisian_records_in_swimming',
        'egypt': 'https://en.wikipedia.org/wiki/List_of_Egyptian_records_in_swimming',
        'africa': 'https://en.wikipedia.org/wiki/List_of_African_records_in_swimming',
        'world': 'https://en.wikipedia.org/wiki/List_of_world_records_in_swimming',
    }
    
    # Create data directories if they don't exist
    os.makedirs('../data/tunisia', exist_ok=True)
    os.makedirs('../data/arab_countries', exist_ok=True)
    os.makedirs('../data/africa', exist_ok=True)
    os.makedirs('../data/world', exist_ok=True)
    
    # Define output paths
    output_paths = {
        'tunisia': ('../data/tunisia/tunisia_swimming_records', 'tunisia'),
        'egypt': ('../data/arab_countries/egypt_swimming_records', 'egypt'),
        'africa': ('../data/africa/africa_swimming_records', 'africa'),
        'world': ('../data/world/world_swimming_records', 'world'),
    }
    
    all_data = {}
    
    # Scrape each source
    for region, url in sources.items():
        records = scrape_swimming_records(url, region)
        if records:
            all_data[region] = records
            display_summary(records, region)
            
            # Save individual files
            base_path, _ = output_paths[region]
            save_to_json(records, f'{base_path}.json')
            save_to_csv(records, f'{base_path}.csv')
    
    # Note about Arab records
    print("\n" + "=" * 60)
    print("NOTE: Arab World Records")
    print("=" * 60)
    print("Wikipedia does not have a dedicated page for Arab swimming records.")
    print("Arab records are typically tracked by individual federations.")
    print("For now, we'll use African records as a comparison point.")
    print("You can manually add Arab records data if available.")
    print("=" * 60)
    
    # Save combined data
    save_to_json(all_data, '../data/all_swimming_records.json')
    
    print("\n✓ Scraping complete!")
    print("\nFiles created:")
    print("  - data/tunisia/tunisia_swimming_records.json/csv")
    print("  - data/arab_countries/egypt_swimming_records.json/csv")
    print("  - data/africa/africa_swimming_records.json/csv")
    print("  - data/world/world_swimming_records.json/csv")
    print("  - data/all_swimming_records.json (combined)")

if __name__ == "__main__":
    main()
