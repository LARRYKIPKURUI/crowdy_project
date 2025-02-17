 # Crowdy - Community Crowdfunding Platform

## Overview
Crowdy is a community-driven crowdfunding platform designed to help individuals and organizations raise funds for public projects. It provides a seamless way to propose, support, and track fundraising campaigns aimed at community improvement.

## Features
- **Project Creation** – Users can create fundraising campaigns for various community projects.
- **Donation System** – Secure payment processing for contributors.
- **Progress Tracking** – Live tracking of funds raised versus target amounts.
- **User Authentication** – Secure sign-up and login functionality.
- **Admin Dashboard** – Manage campaigns, users, and transactions.

## Current Projects
1. **Public Park Cleanup** – Target: Kshs 75,000
2. **Community College Construction** – Target: Kshs 14,100,000
3. **Estate Road Renovation** – Target: Kshs 750,000

## Tech Stack
- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript (React in future updates)
- **Database**: PostgreSQL or SQLite
- **Payment Integration**: [M-Pesa API](https://developer.safaricom.co.ke/) or Stripe
- **Deployment**: Docker, AWS/Heroku

## Installation
### Prerequisites
- Python 3.8+
- Django
- PostgreSQL or SQLite
- Node.js (for frontend if using React)

### Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/LARRYKIPKURUI/crowdy.git
   cd crowdy
   ```
2. Set up a virtual environment and install dependencies:
   ```sh
   python -m venv venv
   source venv/bin/activate  # (Windows: venv\Scripts\activate)
   pip install -r requirements.txt
   ```
3. Run database migrations:
   ```sh
   python manage.py migrate
   ```
4. Start the development server:
   ```sh
   python manage.py runserver
   ```
5. Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

## Contribution
Feel free to contribute by submitting issues or pull requests.

## License
This project is licensed under the MIT License.

