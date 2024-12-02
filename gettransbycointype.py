import requests
import json

# API endpoint and headers
url = "https://api.blockberry.one/sui/v1/coins/0x2%3A%3Asui%3A%3ASUI/transactions?page=0&size=50&orderBy=DESC&sortBy=AGE"
headers = {
    "accept": "*/*",
    "x-api-key": "KMuAxPvXpIy8YD4j25GAI16VsyRTti"
}

# Making the API request
response = requests.post(url, headers=headers, verify=False)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    
    # Extract transaction hashes and calculate total fee
    transaction_hashes = []
    total_fee = 0.0

    for transaction in data.get("content", []):
        # Add the transaction hash to the list
        transaction_hashes.append(transaction.get("txHash"))

        # Add the fee to the total
        fee = transaction.get("fee", 0.0)
        total_fee += fee

    # Display results
    print("Transaction Hashes:")
    print(transaction_hashes)
    print(f"Total Gas Fee: {total_fee}")

    # Optionally, save results to a JSON file
    result = {
        "transaction_hashes": transaction_hashes,
        "total_fee": total_fee
    }

    with open('filtered_transactions.json', 'w') as json_file:
        json.dump(result, json_file, indent=4)
    
    print("Filtered data saved to filtered_transactions.json")
else:
    print(f"Failed to fetch data: {response.status_code} - {response.text}")
