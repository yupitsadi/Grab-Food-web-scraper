#!/bin/bash

# Execute scripts in order
python3 1_webScraper.py
python3 2_RestListFetch.py
python3 3_listMaking.py
python3 4_responceGrab.py


# chmod +x run_scripts.sh  # Make the script executable
# ./run_scripts.sh         # Execute the script
