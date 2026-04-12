import json
from typing import Dict, List
from datetime import datetime

def time_to_seconds(time_str: str) -> float:
    """Convert time string to seconds for comparison"""
    try:
        time_str = time_str.strip()
        
        # Handle minutes:seconds.milliseconds format (e.g., "1:46.44")
        if ':' in time_str:
            parts = time_str.split(':')
            minutes = int(parts[0])
            seconds = float(parts[1])
            return minutes * 60 + seconds
        else:
            # Just seconds.milliseconds format (e.g., "23.03")
            return float(time_str)
    except:
        return float('inf')  # Return infinity if parsing fails

def compare_records(record1: Dict, record2: Dict) -> Dict:
    """Compare two records and return the faster one"""
    time1 = time_to_seconds(record1['time'])
    time2 = time_to_seconds(record2['time'])
    
    if time1 <= time2:
        return record1
    else:
        return record2

def aggregate_arab_records(all_countries_file: str = '../data/arab_countries/all_arab_countries_records.json'):
    """
    Aggregate all Arab countries records to find the best (fastest) time for each event
    """
    print("=" * 70)
    print("ARAB RECORDS AGGREGATOR")
    print("=" * 70)
    
    try:
        with open(all_countries_file, 'r', encoding='utf-8') as f:
            all_countries_data = json.load(f)
    except FileNotFoundError:
        print(f"Error: {all_countries_file} not found!")
        print("Please run 'scrape_arab_countries.py' first.")
        return
    
    print(f"\nLoaded data from {len(all_countries_data)} Arab countries")
    print(f"Countries: {', '.join(all_countries_data.keys())}")
    
    # Structure to hold the best Arab records
    arab_records = {
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
    
    # Track all records by event for comparison
    records_by_event = {}
    
    # Collect all records from all countries
    for country, country_data in all_countries_data.items():
        for course_type in ['long_course', 'short_course']:
            if course_type not in country_data:
                continue
                
            for category in country_data[course_type]:
                records = country_data[course_type][category]
                
                for record in records:
                    event = record['event']
                    key = f"{course_type}_{category}_{event}"
                    
                    if key not in records_by_event:
                        records_by_event[key] = []
                    
                    records_by_event[key].append(record)
    
    print(f"\nFound {len(records_by_event)} unique events across all Arab countries")
    
    # Find the best (fastest) record for each event
    print("\nFinding best Arab records for each event...")
    
    for key, records in records_by_event.items():
        # Key format: "course_type_category_event"
        # Handle both "long_course" and "short_course" properly
        if key.startswith('long_course'):
            course_type = 'long_course'
            rest = key[len('long_course')+1:]  # Remove "long_course_"
        elif key.startswith('short_course'):
            course_type = 'short_course'
            rest = key[len('short_course')+1:]  # Remove "short_course_"
        else:
            continue  # Skip if format is unexpected
        
        # Now split the rest to get category and event
        parts = rest.split('_', 1)
        category = parts[0]
        event = parts[1] if len(parts) > 1 else ''
        
        # Find the fastest record
        best_record = records[0]
        for record in records[1:]:
            best_record = compare_records(best_record, record)
        
        # Add country info and record type
        best_record['record_type'] = 'AR'  # Arab Record
        best_record['region'] = 'Arab World'
        
        # Add to arab_records structure
        if category in arab_records[course_type]:
            arab_records[course_type][category].append(best_record)
    
    # Display summary
    print("\n" + "=" * 70)
    print("ARAB RECORDS SUMMARY")
    print("=" * 70)
    
    total_records = 0
    for course_type in ['long_course', 'short_course']:
        print(f"\n{course_type.replace('_', ' ').title()}:")
        for category in arab_records[course_type]:
            count = len(arab_records[course_type][category])
            total_records += count
            print(f"  {category.replace('_', ' ').title()}: {count} records")
    
    print(f"\nTotal Arab Records: {total_records}")
    
    # Save to JSON
    output_file = '../data/arab_countries/arab_swimming_records.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(arab_records, f, indent=2, ensure_ascii=False)
    
    print(f"\n✓ Arab records saved to: {output_file}")
    
    # Also save a comparison showing which country holds each Arab record
    country_breakdown = {}
    for course_type in arab_records:
        for category in arab_records[course_type]:
            for record in arab_records[course_type][category]:
                country = record['country']
                if country not in country_breakdown:
                    country_breakdown[country] = 0
                country_breakdown[country] += 1
    
    print("\n" + "=" * 70)
    print("ARAB RECORDS BY COUNTRY")
    print("=" * 70)
    sorted_countries = sorted(country_breakdown.items(), key=lambda x: x[1], reverse=True)
    for country, count in sorted_countries:
        percentage = (count / total_records) * 100
        print(f"{country:20} {count:3} records ({percentage:5.1f}%)")
    
    print("\n" + "=" * 70)
    print("✓ Aggregation complete!")
    print("=" * 70)
    
    return arab_records

def main():
    aggregate_arab_records()

if __name__ == "__main__":
    main()
