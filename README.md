# 🏊 Tunisia Swimming Records Database

An interactive web application for comparing Tunisia's national swimming records with Egypt, Africa, Arab nations, and World records. Built with vanilla JavaScript and Python web scraping.

---

## 🚀 Quick Start

### 1. Start the Server
```bash
python start_server.py
```
Or manually:
```bash
python -m http.server 8000
```

### 2. Open in Browser
Visit: **http://localhost:8000/src/index.html**

### 3. Update Records (Optional)
```bash
cd scripts
python scrape_records.py
```

---

## ✨ Features

### 🎯 Main Features
- **6 Interactive Views:**
  - 🇹🇳 Tunisia National Records
  - 🏆 Record Holders - Athletes with multiple national records
  - 🇪🇬 Tunisia vs Egypt Record Comparison
  - 🗺️ Tunisia vs Arab Records Comparison
  - 🌍 Tunisia vs Africa Record Comparison
  - 🌎 Tunisia vs World Record Comparison

- **🏆 Record Holders Feature:**
  - Displays athletes who hold 2+ national swimming records
  - Complete list of each athlete's achievements
  - Event details, times, dates, and locations
  - Clean, professional presentation

- **Comprehensive Data:**
  - Long Course (50m pool) records
  - Short Course (25m pool) records
  - Men's, Women's, and Mixed Relay events
  - Historical data with dates and locations
  - Country flags (80+ countries)
  - 🏊 Swimming style icons

- **Search & Filter:**
  - 🔍 Search by events, swimmers, or countries
  - Filter by Course (Long/Short)
  - Filter by Category (Men/Women)
  - Filter by Event Type (Freestyle, Backstroke, Breaststroke, Butterfly, Medley, Relay)

- **Gap Analysis:**
  - Time difference in seconds
  - Percentage difference
  - Visual indicators showing performance gaps
  - Highlights when Tunisia holds regional or world records

---

## 📊 Data Statistics

### Data Sources:
- All data sourced from Wikipedia swimming records pages
- Updated via Python web scraping scripts
- JSON format for fast loading and processing

### Coverage:
- **Tunisia:** Complete national records database
- **Egypt:** Full national records
- **Arab Countries:** 22 nations including Algeria, Morocco, Saudi Arabia, UAE, Qatar, Egypt, and more
- **Africa:** Continental records
- **World:** Official world swimming records

### Course Types:
- Long Course (50m pools)
- Short Course (25m pools)

### Categories:
- Men's events
- Women's events
- Mixed relays

---

## 🎨 Visual Design

### Modern Water-Inspired Theme:
- **Background:** Calming pool water gradient (light to medium blue)
- **Cards:** Clean white cards with soft shadows
- **Accents:** Deep ocean blue (#005b9f) for buttons and highlights
- **Typography:** Modern system fonts for readability

### Regional Color Coding (Table Headers):
- 🇹🇳 **Tunisia:** Ocean Blue (#005b9f)
- 🇪🇬 **Egypt:** Brown (#b45309)
- 🗺️ **Arab:** Green (#047857)
- 🌍 **Africa:** Orange (#d97706)
- 🌎 **World:** Blue (#1d4ed8)

### Accessibility:
- High contrast text for readability
- Country flags for visual identification
- Clear event categorization
- Responsive design for mobile devices
- Search functionality

---

## 📁 Project Structure

```
tunisia-swimming-records/
├── src/                              # Web application
│   ├── index.html                    # Landing page
│   ├── compare.html                  # Records comparison
│   ├── display_records.html          # Records display
│   ├── medals.html                   # Olympic medals
│   └── rising_stars.html             # Young talent recognition (NEW!)
│
├── data/                             # All data files
│   ├── tunisia/                      # Tunisia records
│   │   ├── tunisia_swimming_records.json
│   │   └── tunisia_swimming_records.csv
│   ├── arab_countries/               # Arab nations records
│   │   ├── egypt_swimming_records.json
│   │   ├── arab_swimming_records.json
│   │   └── all_arab_countries_records.json
│   ├── africa/                       # African records
│   │   ├── africa_swimming_records.json
│   │   └── africa_swimming_records.csv
│   ├── world/                        # World records
│   │   ├── world_swimming_records.json
│   │   └── world_swimming_records.csv
│   ├── athlete_medals.json           # Medal data
│   └── all_swimming_records.json     # Combined data
│
├── scripts/                          # Python scraping scripts
│   ├── scrape_records.py             # Main scraper
│   ├── scrape_arab_countries.py      # Arab countries scraper
│   ├── aggregate_arab_records.py     # Arab records aggregator
│   └── scrape_medals.py              # Medals scraper
│
├── .gitignore                        # Git ignore file
├── README.md                         # This file
├── requirements.txt                  # Python dependencies
└── start_server.py                   # Quick server launcher
```

---

## 💻 How to Use

### Navigation:
1. **Record Holders** 🏆 - View athletes with multiple national records
2. **Tunisia Records** - Browse all national records
3. **Comparison Views** - Compare with Egypt, Arab nations, Africa, or World records
4. **Filters** - Filter by course type, category, or event
5. **Search** - Find specific events, swimmers, or records

### Features Overview:
- **Record Holders Page** - Displays athletes who hold 2+ national records
- **Gap Analysis** - Percentage and time differences between records
- **Search Functionality** - Search by event, swimmer name, or country
- **Course Filtering** - Separate Long Course (50m) and Short Course (25m) views

---

## 🔧 Technical Details

### Requirements:
- Python 3.6+
- Libraries: `requests`, `beautifulsoup4`, `lxml`

### Installation:
```bash
pip install requests beautifulsoup4 lxml
```

### Data Sources:
- Wikipedia - Tunisian swimming records
- Wikipedia - Egyptian swimming records
- Wikipedia - African swimming records
- Wikipedia - World swimming records

### Event Name Normalization:
The scraper automatically normalizes event names to ensure proper matching:
- Converts "4 × 100 m" to "4x100m"
- Standardizes spacing and symbols
- Handles multiple format variations

### Time Parsing:
Smart time parsing handles:
- Simple seconds: `23.45`
- Minutes: `1:23.45`
- Hours (rare): `1:05:23.45`
- Auto-detects misformatted times (3:20:12 → 3:20.12)

---

## 🎯 Understanding the Interface

### Record Highlighting:
- **Light blue highlighting:** Tunisia holds the record or has competitive performance
- Indicates current record holder status

### Data Completeness:
- (!) indicator shows missing data  
- Hover to see which fields are incomplete
- Typically date, location, or meet information

### Search Functionality:
- Search by **event name**: "freestyle", "butterfly"
- Search by **swimmer name**: Last name or full name
- Search by **country code**: "USA", "CHN", "EGY"
- Search by **location**: City or venue name

---

## 🚀 Updates & Maintenance

### Update All Records:
```bash
cd scripts
python scrape_records.py
```
This fetches the latest data from Wikipedia for all countries.

### Server Management:

**Quick Start (Recommended):**
```bash
python start_server.py
```
This automatically opens your browser to the correct page.

**Manual Start:**
```bash
python -m http.server 8000
# Then visit http://localhost:8000/src/index.html
```

**Stop:**
Press `Ctrl+C` in terminal

**Different Port:**
```bash
python -m http.server 8002
# Then visit http://localhost:8002/src/index.html
```

---

## 🎓 Understanding the Data

### Gap Analysis:
Shows performance difference between Tunisia and comparison records:
- **Negative gap** (green with 🚀) = Tunisia has the faster time
- **Small gap** (<2%, green) = Close performance
- **Medium gap** (2-5%, yellow) = Moderate difference
- **Large gap** (>5%, red) = Significant difference

### Record Comparison:
Compare Tunisia's national records with:
- **Egypt** - Regional comparison (North Africa)
- **Arab Nations** - Best times from 22 Arab countries
- **Africa** - Continental records
- **World** - Global records

---

## 🛠️ Troubleshooting

### Issue: "Error loading records"
**Solution:** Make sure you're running the local server:
```bash
python start_server.py
```
Don't open HTML files directly (CORS restrictions require a server).

### Issue: Port already in use
**Solution:** Change the port:
```bash
python -m http.server 8002
# Then visit http://localhost:8002/src/index.html
```

### Issue: No records displayed
**Solution:** 
1. Verify JSON files exist in `data/` directories
2. Run the scraper: `cd scripts && python scrape_records.py`
3. Refresh the browser

### Issue: Search not working
**Solution:** Refresh page and clear browser cache (Ctrl+F5)

### Issue: Incorrect time formatting
**Solution:** Re-run the scraper to fix formatting:
```bash
cd scripts
python scrape_records.py
```

---

## 📜 Credits & License

### Data Sources:
- [Wikipedia - Tunisia Swimming Records](https://en.wikipedia.org/wiki/List_of_Tunisian_records_in_swimming)
- [Wikipedia - Egypt Swimming Records](https://en.wikipedia.org/wiki/List_of_Egyptian_records_in_swimming)
- [Wikipedia - Africa Swimming Records](https://en.wikipedia.org/wiki/List_of_African_records_in_swimming)
- [Wikipedia - World Swimming Records](https://en.wikipedia.org/wiki/List_of_world_records_in_swimming)

### License:
Data sourced from Wikipedia under Creative Commons Attribution-ShareAlike 4.0 License.

### Project:
Educational tool for swimming records analysis and comparison.

---

**Built with Python and Vanilla JavaScript** 🇹🇳

**Visit:** http://localhost:8000/src/index.html

**Last Updated:** April 2026


---

*Data sourced from Wikipedia swimming records | Pool types: Long Course (50m) and Short Course (25m)*
