# Football Pro 98 `.lge` File Extraction

This project helps you extract readable team names (and other info) from the `.lge` save files used by Sierra's Football Pro 98.

## How it works

- Finds `T03:` team blocks in the `.lge` file.
- Decrypts each block using a simple XOR algorithm.
- Extracts all readable ASCII strings (team names, stadiums, coaches).
- Filters output for known NFL teams.

## Usage

1. Place your `NFLPI97.lge` file in the same directory as the script.
2. Run the Python script:  
   `python extract_nflpi_team_names.py`
3. View results in your terminal.

## Notes on `.lge` file structure

- Team records start after the bytes `T03:`.
- Block decryption uses a simple XOR based on the team block ID.
- Team names and other info may only appear for edited or active teams.

## Example output

```
NFL teams found in extracted strings:
Found NFL team: Seahawks
```

## Credits

Based on reverse engineering and community help.