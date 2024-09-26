```
# Automated Daily Stripe Payouts

This Python script automates daily payouts from your Stripe account to a connected bank account in Indian Rupees (INR). It uses the Stripe API to initiate a payout at 1 PM IST every day. The script is designed to be run in conjunction with a task scheduler like `cron` or Windows Task Scheduler.

## Features
- Automates payouts in INR to a connected bank account.
- Uses the Stripe API for secure transactions.
- Daily execution at a specified time (1 PM IST) through task scheduling.
- Handles environment variables securely using a `.env` file.

## Requirements

### 1. Python Libraries
The script relies on the following Python libraries:
- [Stripe Python SDK](https://pypi.org/project/stripe/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

These can be installed by running the following command:
```bash
pip install -r requirements.txt
```

### 2. Stripe Account
To use this script, you need:
- A Stripe account with available funds.
- A connected bank account in your Stripe dashboard.
- Your Stripe secret API key.

### 3. Python Version
This script is compatible with **Python 3.x**.

## Setup Instructions

### 1. Clone the Repository
Clone this repository to your local machine:
```bash
git clone https://github.com/yourusername/stripe-automated-payouts.git
cd stripe-automated-payouts
```

### 2. Set Up Environment Variables
Create a `.env` file in the root directory of your project and add your environment variables:
```bash
STRIPE_API_KEY=your_stripe_secret_api_key
BANK_ACCOUNT_ID=your_connected_bank_account_id
AMOUNT=100000  # Amount in paise (for ₹1000, set it to 100000)
```

### 3. Install Dependencies
Install the required Python packages:
```bash
pip install -r requirements.txt
```

### 4. Running the Script
You can manually run the script to test it:
```bash
python daily_payout.py
```

### 5. Schedule the Script to Run Daily
To automate the script to run at 1 PM IST every day, use a task scheduler. Here are instructions for different operating systems:

#### Linux/Mac (using `cron`):
1. Open your crontab file for editing:
   ```bash
   crontab -e
   ```
2. Add the following line to schedule the script to run at 1 PM IST every day:
   ```bash
   30 7 * * * /usr/bin/python3 /path/to/your/project/daily_payout.py
   ```

#### Windows (using Task Scheduler):
1. Open **Task Scheduler**.
2. Create a new task and set it to run daily at 1 PM IST.
3. Under the **Actions** tab, select "Start a Program" and point to `python.exe`, passing the script's path as an argument.

## Project Structure

```bash
├── daily_payout.py        # Main Python script for automating the payout
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (DO NOT COMMIT this file)
└── README.md              # Project documentation
```

## Configuration

### .env File

You need to configure your `.env` file with the following variables:
- **STRIPE_API_KEY**: Your Stripe secret API key.
- **BANK_ACCOUNT_ID**: The connected bank account ID in your Stripe dashboard.
- **AMOUNT**: The amount to be paid out, in the smallest unit of currency (paise for INR).

Example:
```env
STRIPE_API_KEY=sk_test_xxxxxxxxxxxxxxxxxx
BANK_ACCOUNT_ID=ba_xxxxxxxxxxxxx
AMOUNT=100000  # ₹1000 in paise
```

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contributing
If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are welcome.

## Contact
For issues, questions, or feedback, please contact: [mrinalbhoumick0610@gmail.com](mailto:mrinalbhoumick0610@gmail.com).
```