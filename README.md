# 🏊 Tunisia Swimming Records

Hey! This is a web app I built to track Tunisia's national swimming records and compare them with other countries around the world.

## Why I built this

As someone passionate about both web development and Tunisian sports, I wanted to create something useful for our swimming community. Coaches and athletes can now quickly see where Tunisia stands compared to Egypt, other Arab countries, Africa, and world records—all in one place.

## What it does

**The main feature:** You can compare Tunisia's swimming records side-by-side with any other country. The app shows you exactly how close (or far) we are from breaking regional or world records.

**Other cool stuff:**
- See which Tunisian athletes hold multiple national records
- Search for specific events, swimmers, or countries
- Filter by pool type (25m or 50m), gender, or swimming style
- Dynamic country selector that auto-updates when new data is added
- Gap analysis showing time differences and percentages

## Getting started

**To run it locally:**

```bash
python start_server.py
```

Then open your browser and go to `http://localhost:8000/src/index.html`

That's it!

**Want to update the records?**

```bash
cd scripts
python scrape_records.py
```

## How it works

The app uses vanilla JavaScript for the frontend (no frameworks—keeping it simple) and Python scripts to scrape swimming records from Wikipedia. All the data is stored in JSON files, so it loads super fast.

I built a cool auto-detection system: when you add a new country's JSON file to the `data/arab_countries/` folder, it automatically shows up in the comparison dropdown. No code changes needed.

## What's inside

- **Tunisia's complete records** (long course + short course)
- **22 Arab countries** for comparison
- **African continental records**
- **World records**
- **Clean, modern UI** with professional swimmer photos

## The tech stack

- HTML/CSS/JavaScript (vanilla, no libraries)
- Python for web scraping
- Wikipedia as the data source
- Just a simple HTTP server to run it

## Contributing

Found a mistake in the records? Want to add more countries? Pull requests are welcome! The scraping scripts are in the `/scripts` folder.

## Future ideas

Things I might add later:
- Mobile app version
- Export/share specific comparisons
- Trend analysis over time
- Training goal calculator based on gap analysis

---

Built with 🏊 for the Tunisian swimming community

**Questions or suggestions?** Open an issue or reach out!

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
