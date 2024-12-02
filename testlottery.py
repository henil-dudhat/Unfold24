import json
import random

# Load filtered transaction data
with open('filtered_transactions.json', 'r') as file:
    data = json.load(file)

transaction_hashes = data['transaction_hashes']
total_gas_fee = data['total_fee']

# Calculate odds of winning
winning_odds = 0.025  # 2.5%

# Perform lucky draw
def perform_lucky_draw(hashes, odds):
    for tx_hash in hashes:
        if random.random() < odds:  # Randomly determine if this hash wins
            return tx_hash
    return None  # No winner if no hash meets the odds

# Execute lottery system
winner = perform_lucky_draw(transaction_hashes, winning_odds)

if winner:
    # Calculate prize and burned amounts
    prize = total_gas_fee * 0.7
    burned = total_gas_fee * 0.3
    print(f"Winner Selected: {winner}")
    print(f"Prize Allocated: {prize}")
    print(f"Amount Burned: {burned}")
else:
    # No winner, carry forward the total gas fee
    print("No winner selected. Gas fee pool carried forward.")
    print(f"Carry Forward: {total_gas_fee}")
