# Adding New Countries for Comparison

This guide explains how to add new country swimming records to the comparison system.

## Quick Start

1. **Scrape the Data**
   ```bash
   cd scripts
   python scrape_arab_countries.py
   ```
   This script automatically scrapes swimming records from Wikipedia for all Arab countries.

2. **Data is Auto-Detected**
   Once you have a JSON file in the `data/arab_countries/` folder with the naming pattern `{country}_swimming_records.json`, it will automatically appear in the comparison dropdown!

## File Structure

Place new country data files in:
```
data/arab_countries/{country}_swimming_records.json
```

## Supported Countries (Auto-detected)

The system automatically checks for these countries:
- 🇪🇬 Egypt
- 🇩🇿 Algeria  
- 🇲🇦 Morocco
- 🇸🇦 Saudi Arabia
- 🇦🇪 UAE
- 🇯🇴 Jordan
- 🇱🇧 Lebanon
- 🇮🇶 Iraq
- 🇸🇾 Syria
- 🇶🇦 Qatar
- 🇰🇼 Kuwait
- 🇧🇭 Bahrain
- 🇴🇲 Oman
- 🇵🇸 Palestine

## JSON Format

Each country file should follow this structure:

```json
{
  "long_course": {
    "men": [
      {
        "event": "50 m freestyle",
        "time": "22.50",
        "swimmer": "Athlete Name",
        "date": "1 January 2024",
        "location": "City, Country"
      }
    ],
    "women": [...],
    "mixed": [...]
  },
  "short_course": {
    "men": [...],
    "women": [...],
    "mixed": [...]
  }
}
```

## Adding a Non-Arab Country

To add countries outside the Arab world:

1. Create a new folder: `data/other_countries/`
2. Update `loadAvailableCountries()` in `src/compare.html` to check this folder
3. Add the country to the `potentialCountries` array:

```javascript
{ 
  key: 'spain', 
  name: '🇪🇸 Spain', 
  file: 'spain_swimming_records.json', 
  folder: 'other_countries' 
}
```

## How It Works

1. On page load, the system tries to fetch each country's JSON file
2. If the file exists and loads successfully, it's added to `availableCountries`
3. The dropdown is automatically populated with available countries
4. Users can select any country for head-to-head comparison with Tunisia

## Benefits

- **No Code Changes Needed**: Just add JSON files
- **Extensible**: Works with any country data
- **Automatic**: System detects new files on page load
- **User-Friendly**: Clean dropdown interface

## Testing

After adding new country data:

1. Refresh the compare page
2. Look for the dropdown: "Or compare with specific country:"
3. Your new country should appear in the list
4. Select it to see Tunisia vs that country

## Notes

- Egypt appears in both the main tabs and the dropdown (for consistency)
- Countries are sorted alphabetically in the dropdown
- Only successfully loaded countries appear
- Missing data files are silently skipped (no errors)
