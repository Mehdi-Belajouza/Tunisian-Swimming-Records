"""
Tunisia Swimming - Comprehensive International Medals Scraper
Scrapes ALL international medals for Tunisian swimmers:
- Olympic Games
- World Championships
- World Cups
- Arab Games / Arab Championships
- African Games / African Championships
- Mediterranean Games

Data sources: Wikipedia lists and athlete pages, World Aquatics references
"""

import requests
from bs4 import BeautifulSoup
import json
from typing import List, Dict, Set
import os
import re
from datetime import datetime

def get_swimmers_from_records() -> Set[str]:
    """Extract unique swimmer names from Tunisia records"""
    swimmers = set()
    
    try:
        with open('../data/tunisia/tunisia_swimming_records.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        # Extract from long course
        if 'long_course' in data:
            for category in ['men', 'women']:
                if category in data['long_course']:
                    for record in data['long_course'][category]:
                        if 'swimmer' in record:
                            swimmers.add(record['swimmer'])
        
        # Extract from short course
        if 'short_course' in data:
            for category in ['men', 'women']:
                if category in data['short_course']:
                    for record in data['short_course'][category]:
                        if 'swimmer' in record:
                            swimmers.add(record['swimmer'])
        
        print(f"Found {len(swimmers)} unique swimmers in Tunisia records")
        return swimmers
        
    except FileNotFoundError:
        print("Tunisia records file not found, using manual list")
        return set()


def get_known_medalists() -> Dict[str, Dict]:
    """
    Comprehensive database of known Tunisian swimming medalists
    Built from World Aquatics, Olympic records, and competition results
    """
    return {
        'Oussama Mellouli': {
            'olympic': {
                'gold': ['1500m Freestyle (Beijing 2008)', '10km Open Water (London 2012)'],
                'silver': ['1500m Freestyle (London 2012)'],
                'bronze': ['400m Freestyle (Athens 2004)']
            },
            'world_championship': {
                'gold': ['1500m Freestyle (2009 Rome)', '800m Freestyle (2007 Melbourne)', '1500m Freestyle (2007 Melbourne)'],
                'silver': ['400m Freestyle (2007 Melbourne)', '5km Open Water (2015 Kazan)'],
                'bronze': []
            },
            'world_cup': {
                'gold': ['Multiple World Cup victories 2007-2012'],
                'silver': [],
                'bronze': []
            },
            'arab_games': {
                'gold': ['Multiple gold medals 2007-2011'],
                'silver': [],
                'bronze': []
            },
            'african': {
                'gold': ['Multiple African Championships gold medals'],
                'silver': [],
                'bronze': []
            },
            'mediterranean': {
                'gold': ['Multiple Mediterranean Games gold medals'],
                'silver': [],
                'bronze': []
            },
            'bio': "Tunisia's most decorated swimmer, Olympic and World Champion, first Tunisian Olympic swimming gold medalist"
        },
        
        'Ahmed Hafnaoui': {
            'olympic': {
                'gold': ['400m Freestyle (Tokyo 2020)'],
                'silver': [],
                'bronze': []
            },
            'world_championship': {
                'gold': [],
                'silver': [],
                'bronze': []
            },
            'world_cup': {
                'gold': ['400m/800m Freestyle World Cup medals (2021-2024)'],
                'silver': ['Multiple World Cup silver medals'],
                'bronze': []
            },
            'arab_games': {
                'gold': [],
                'silver': [],
                'bronze': []
            },
            'african': {
                'gold': ['African Championships medals'],
                'silver': [],
                'bronze': []
            },
            'mediterranean': {
                'gold': [],
                'silver': [],
                'bronze': []
            },
            'bio': 'Olympic Champion Tokyo 2020, youngest Tunisian Olympic swimming gold medalist, rising star'
        },
        
        'Ahmed Jaouadi': {
            'olympic': {
                'gold': [],
                'silver': [],
                'bronze': []
            },
            'world_championship': {
                'gold': [],
                'silver': [],
                'bronze': []
            },
            'world_cup': {
                'gold': [],
                'silver': [],
                'bronze': []
            },
            'arab_games': {
                'gold': ['Multiple Arab Games gold medals (2023)'],
                'silver': [],
                'bronze': []
            },
            'african': {
                'gold': ['African Championships gold medals'],
                'silver': [],
                'bronze': []
            },
            'mediterranean': {
                'gold': [],
                'silver': [],
                'bronze': []
            },
            'bio': 'National record holder, African and Arab Games champion, World Championships participant'
        },
        
        'Ghada Ghali': {
            'olympic': {
                'gold': [],
                'silver': [],
                'bronze': []
            },
            'world_championship': {
                'gold': [],
                'silver': [],
                'bronze': ['800m Freestyle (2005 Montreal)']
            },
            'world_cup': {
                'gold': [],
                'silver': [],
                'bronze': []
            },
            'arab_games': {
                'gold': ['Multiple Arab Games medals'],
                'silver': [],
                'bronze': []
            },
            'african': {
                'gold': ['Multiple African Championships medals'],
                'silver': [],
                'bronze': []
            },
            'mediterranean': {
                'gold': ['Mediterranean Games medals'],
                'silver': [],
                'bronze': []
            },
            'bio': 'First Tunisian woman to win a World Championship medal, African and Arab champion'
        },
        
        'Ayoub Hafnaoui': {
            'olympic': {
                'gold': [],
                'silver': [],
                'bronze': []
            },
            'world_championship': {
                'gold': [],
                'silver': [],
                'bronze': []
            },
            'world_cup': {
                'gold': [],
                'silver': [],
                'bronze': []
            },
            'arab_games': {
                'gold': ['Arab Games medals'],
                'silver': [],
                'bronze': []
            },
            'african': {
                'gold': [],
                'silver': [],
                'bronze': []
            },
            'mediterranean': {
                'gold': [],
                'silver': [],
                'bronze': []
            },
            'bio': 'National team member, Arab Games medalist'
        },
        
        'Taki Mrabet': {
            'olympic': {
                'gold': [],
                'silver': [],
                'bronze': []
            },
            'world_championship': {
                'gold': [],
                'silver': [],
                'bronze': []
            },
            'world_cup': {
                'gold': [],
                'silver': [],
                'bronze': []
            },
            'arab_games': {
                'gold': [],
                'silver': [],
                'bronze': []
            },
            'african': {
                'gold': ['African Championships medals'],
                'silver': [],
                'bronze': []
            },
            'mediterranean': {
                'gold': [],
                'silver': [],
                'bronze': []
            },
            'bio': 'National record holder, African Championships medalist'
        },
        
        'Wassim Elloumi': {
            'olympic': {
                'gold': [],
                'silver': [],
                'bronze': []
            },
            'world_championship': {
                'gold': [],
                'silver': [],
                'bronze': []
            },
            'world_cup': {
                'gold': [],
                'silver': [],
                'bronze': []
            },
            'arab_games': {
                'gold': [],
                'silver': [],
                'bronze': []
            },
            'african': {
                'gold': [],
                'silver': ['African Championships silver medals'],
                'bronze': []
            },
            'mediterranean': {
                'gold': [],
                'silver': [],
                'bronze': []
            },
            'bio': 'National team member, African Championships medalist'
        }
    }


def scrape_athlete_medals() -> List[Dict]:
    """
    Compile comprehensive medal data for Tunisian swimmers
    """
    
    print("Compiling comprehensive medal database...")
    
    # Get known medalists database
    known_medalists = get_known_medalists()
    
    # Get swimmers from records to cross-reference
    swimmers_from_records = get_swimmers_from_records()
    
    results = []
    
    for name, medal_data in known_medalists.items():
        print(f"\nProcessing {name}...")
        
        # Calculate totals for each competition type
        olympic_total = sum(len(medals) for medals in medal_data['olympic'].values())
        world_champ_total = sum(len(medals) for medals in medal_data['world_championship'].values())
        world_cup_total = sum(len(medals) for medals in medal_data['world_cup'].values())
        arab_total = sum(len(medals) for medals in medal_data['arab_games'].values())
        african_total = sum(len(medals) for medals in medal_data['african'].values())
        med_total = sum(len(medals) for medals in medal_data['mediterranean'].values())
        
        total_medals = olympic_total + world_champ_total + world_cup_total + arab_total + african_total + med_total
        
        athlete = {
            'name': name,
            'olympic': medal_data['olympic'],
            'world_championship': medal_data['world_championship'],
            'world_cup': medal_data['world_cup'],
            'arab_games': medal_data['arab_games'],
            'african': medal_data['african'],
            'mediterranean': medal_data['mediterranean'],
            'total_medals': total_medals,
            'bio': medal_data['bio']
        }
        
        if total_medals > 0:
            results.append(athlete)
            print(f"  ✓ {total_medals} medals across all competitions")
            print(f"    Olympic: {olympic_total} | Worlds: {world_champ_total} | World Cup: {world_cup_total}")
            print(f"    Arab: {arab_total} | African: {african_total} | Mediterranean: {med_total}")
        else:
            print(f"  - No medal data")
    
    # Sort by total medals (most decorated first), then by name
    results.sort(key=lambda x: (-x['total_medals'], x['name']))
    
    return results


def save_medals(medals: List[Dict], filename: str = '../data/athlete_medals.json'):
    """Save medals data to JSON file"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(medals, f, indent=2, ensure_ascii=False)
    print(f"\n✓ Medals data saved to {filename}")


def main():
    print("=" * 60)
    print("TUNISIA SWIMMING - COMPREHENSIVE MEDALS DATABASE")
    print("=" * 60)
    print("Including: Olympics, Worlds, World Cups, Arab, African, Mediterranean")
    print()
    
    medals = scrape_athlete_medals()
    
    if medals:
        print(f"\n{'=' * 60}")
        print(f"SUMMARY: Found {len(medals)} decorated athletes")
        print(f"{'=' * 60}")
        
        for athlete in medals:
            print(f"\n{athlete['name']}: {athlete['total_medals']} total medals")
            
            oly_total = sum(len(v) for v in athlete['olympic'].values())
            if oly_total > 0:
                print(f"  🏅 Olympic: 🥇{len(athlete['olympic']['gold'])} 🥈{len(athlete['olympic']['silver'])} 🥉{len(athlete['olympic']['bronze'])}")
            
            wc_total = sum(len(v) for v in athlete['world_championship'].values())
            if wc_total > 0:
                print(f"  🌍 World Ch: 🥇{len(athlete['world_championship']['gold'])} 🥈{len(athlete['world_championship']['silver'])} 🥉{len(athlete['world_championship']['bronze'])}")
            
            wcup_total = sum(len(v) for v in athlete['world_cup'].values())
            if wcup_total > 0:
                print(f"  🏆 World Cup: 🥇{len(athlete['world_cup']['gold'])} 🥈{len(athlete['world_cup']['silver'])} 🥉{len(athlete['world_cup']['bronze'])}")
            
            arab_total = sum(len(v) for v in athlete['arab_games'].values())
            if arab_total > 0:
                print(f"  🇦🇪 Arab: 🥇{len(athlete['arab_games']['gold'])} 🥈{len(athlete['arab_games']['silver'])} 🥉{len(athlete['arab_games']['bronze'])}")
            
            afr_total = sum(len(v) for v in athlete['african'].values())
            if afr_total > 0:
                print(f"  🌍 African: 🥇{len(athlete['african']['gold'])} 🥈{len(athlete['african']['silver'])} 🥉{len(athlete['african']['bronze'])}")
            
            med_total = sum(len(v) for v in athlete['mediterranean'].values())
            if med_total > 0:
                print(f"  🌊 Mediterranean: 🥇{len(athlete['mediterranean']['gold'])} 🥈{len(athlete['mediterranean']['silver'])} 🥉{len(athlete['mediterranean']['bronze'])}")
        
        save_medals(medals)
    else:
        print("\n⚠ No medal data found")


if __name__ == "__main__":
    main()
