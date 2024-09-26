import os
from dotenv import load_dotenv
import requests
from datetime import datetime

load_dotenv()

def perform_transaction():
    to_account = os.getenv('TO_ACCOUNT')
    from_account = os.getenv('FROM_ACCOUNT')
    amount = os.getenv('AMOUNT')
    bank_api_key = os.getenv('BANK_API_KEY')
    headers = {
        'Authorization': f'Bearer {bank_api_key}',
        'Content-Type': 'application/json'
    }
    payload = {
        'from_account': from_account,
        'to_account': to_account,
        'amount': amount,
        'currency': 'INR',
        'note': 'Daily automated transfer in INR'
    }
    print(f"Initiating transfer of ₹{amount} from {from_account} to {to_account} at {datetime.now()}")

    try:
        response = requests.post('https://api.bank.com/transfer', json=payload, headers=headers)

        if response.status_code == 200:
            print("Transaction successful!")
        else:
            print(f"Failed to transfer: {response.status_code}, {response.text}")
    except Exception as e:
        print(f"Error occurred during transaction: {e}")
if __name__ == "__main__":
    perform_transaction()
