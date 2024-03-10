import json

# Specify the path to your JSON file
json_file_path = r'combined_list.txt'
output_file_path = r'combined_listArray.txt'

try:
    # Read the JSON content
    with open(json_file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    # Extract data from "getRecommendedMerchantsV2" and "getRestaurantsV2"
    recommended_merchants = data.get("getRecommendedMerchantsV2/countryCode=SG&latitude=1.287953&longitude=103.851784", {}).get("getRecommendedMerchantsV2/countryCode=SG&latitude=1.287953&longitude=103.851784", [])
    restaurant_list = data.get("getRestaurantsV2/countryCode=SG&latlng=1.287953%2C103.851784", {}).get("getRestaurantsV2/countryCode=SG&latlng=1.287953%2C103.851784", [])

    # Combine both lists into a single list
    combined_list = recommended_merchants + restaurant_list

    # Print or process the combined list as needed
    print("Combined List Array:", combined_list)

    # Store the combined list as a JSON array in a text file
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        json.dump(combined_list, output_file, indent=2)

    print(f"Combined list stored in '{output_file_path}'")

except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")

except FileNotFoundError:
    print(f"Error: File not found at path '{json_file_path}'")

