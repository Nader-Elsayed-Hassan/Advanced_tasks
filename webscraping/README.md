# Jumia scrapper (task.py)

This small scraper script fetches product name, price and product link from Jumia Egypt search results for "phone".

How to run

1. Make sure you have Python 3.8+.
2. Install required packages (requests, beautifulsoup4, pandas). Optionally install openpyxl if you want Excel output.

```powershell
python -m pip install requests beautifulsoup4 pandas
# optional, enable Excel writer
python -m pip install openpyxl
```

3. Run the script:

```powershell
python task.py
```

- Behavior and Notes

- The code now:
	1. sets a User-Agent header to reduce blocking
	2. guards against missing anchor/href to avoid KeyError
	3. prefers Excel (.xlsx) output. If openpyxl isn't installed the script will try to install it automatically at runtime. If that auto-install fails (no network or permission issues), it will fall back to CSV output.
- Output files will be created in the same folder as the script: `jumia_products.xlsx` (if openpyxl installed) or `jumia_products.csv` (fallback).
 - Output files will be created in the same folder as the script: `jumia_products.xlsx` (preferred) or `jumia_products.csv` (fallback).

If you want me to also add unit tests or improve selection (e.g., handle pagination), tell me and I can extend this further.