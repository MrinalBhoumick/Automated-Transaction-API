import os
import stripe
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

stripe.api_key = os.getenv('STRIPE_API_KEY')

def perform_payout():
    amount = int(os.getenv('AMOUNT'))  # Amount in paise (₹1000 = 100000 paise)
    currency = "INR"
    bank_account_id = os.getenv('BANK_ACCOUNT_ID')

    try:
        payout = stripe.Payout.create(
            amount=amount,  # Amount in paise
            currency=currency,
            destination=bank_account_id,
            method="standard",
            description="Daily automated payout to bank in INR"
        )

        print(f"✅ Initiated payout of ₹{amount / 100:.2f} to bank account at {datetime.now()}")
        print(f"Payout ID: {payout.id}")
    except Exception as e:
        print(f"❌ Error occurred during payout: {e}")

if __name__ == "__main__":
    perform_payout()
