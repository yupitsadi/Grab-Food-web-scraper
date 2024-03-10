import os
import json
import gzip
import requests

# Read IDs from the combined_listArray.txt file
combined_list_file_path = "combined_listArray.txt"
with open(combined_list_file_path, "r", encoding="utf-8") as combined_list_file:
    ids = json.load(combined_list_file)

# Fetching responses and saving to individual JSON files
url_template = "https://portal.grab.com/foodweb/v2/merchants/{}"
output_folder = "responses"
os.makedirs(output_folder, exist_ok=True)

for merchant_id in ids:
    url = url_template.format(merchant_id)
    response = requests.get(url)
    
    output_file_path = os.path.join(output_folder, f"{merchant_id}_response.json")
    with open(output_file_path, "w", encoding="utf-8") as output_file:
        output_file.write(response.text)

    print(f"Response for ID {merchant_id} saved to {output_file_path}")

# Extracting data
all_data = []

for merchant_id in ids:
    input_file_path = os.path.join(output_folder, f"{merchant_id}_response.json")
    
    with open(input_file_path, "r", encoding="utf-8") as input_file:
        data = json.load(input_file)
        merchant_info = data.get("merchant", {})
        
        # Extract specific fields
        merchant_id = merchant_info.get("ID")
        name = merchant_info.get("name")
        cuisine = merchant_info.get("cuisine")
        timezone = merchant_info.get("timeZone")
        photo_href = merchant_info.get("photoHref")
        eta = merchant_info.get("ETA")
        latlng = merchant_info.get("latlng")
        rating = merchant_info.get("Rating")
        distance_in_km = merchant_info.get("distanceInKm")
        
        estimated_delivery_fee = merchant_info.get("estimatedDeliveryFee", {})
        currency = estimated_delivery_fee.get("currency")
        price = estimated_delivery_fee.get("price")
        price_display = estimated_delivery_fee.get("priceDisplay")
        status = estimated_delivery_fee.get("status")
        multiplier = estimated_delivery_fee.get("Multiplier")
        
        promotions = merchant_info.get("promotions")

        all_data.append({
            "ID": merchant_id,
            "Details": {
                "Name": name,
                "Cuisine": cuisine,
                "TimeZone": timezone,
                "PhotoHref": photo_href,
                "ETA": eta,
                "Latlng": latlng,
                "Rating": rating,
                "DistanceInKm": distance_in_km,
                "EstimatedDeliveryFee": {
                    "Currency": currency,
                    "Price": price,
                    "PriceDisplay": price_display,
                    "Status": status,
                    "Multiplier": multiplier,
                },
                "Promotions": promotions,
                # Add more fields here
            }
        })

# Save all extracted data to a single compressed (gzip) ndjson file in the main directory
output_file_path = "all_responses.ndjson.gz"
with gzip.open(output_file_path, "wt", encoding="utf-8") as output_file:
    for data in all_data:
        json.dump(data, output_file, indent=4)
        output_file.write('\n')

print(f"All responses saved to individual JSON files and extracted data saved to {output_file_path}")
