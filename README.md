# Digital Heroes Charity Golf Platform

A modern full-stack Django web application that combines golf score tracking, charity fundraising, and reward-based monthly draws. Users can track their golf performance, support charities, participate in prize draws, and manage subscriptions through a secure and interactive platform.

---

## Project Overview

Digital Heroes is a subscription-driven platform designed to create social impact through sports participation. Users enter golf scores, contribute to charitable causes, and become eligible for monthly prize draws.

The platform focuses on:

- Golf Score Management
- Charity Contributions
- Monthly Reward Draws
- Winner Verification
- Subscription Management
- Analytics & Reporting

---

## Features

### Authentication System

- User Registration
- User Login
- User Logout
- Secure Authentication
- User Profile Management

---

### Dashboard

- Personalized Dashboard
- Total Scores Overview
- Draw Participation Summary
- Winnings Overview
- Selected Charity Information
- Subscription Status
- Recent Scores Display
- Score Analytics Chart

---

### Score Management

- Add Golf Scores
- Edit Scores
- Delete Scores
- Duplicate Date Validation
- Maximum 5 Scores Retained
- Automatic Removal of Oldest Score
- Reverse Chronological Display

---

### Subscription System

- Monthly Subscription Plan
- Yearly Subscription Plan
- Razorpay Payment Integration
- Subscription Status Tracking
- Renewal Date Tracking
- Active / Inactive Subscription Status

---

### Charity System

- Charity Listing
- Charity Search
- Charity Selection
- Donation Percentage Tracking
- Featured Charity Section

---

### Draw System

- Monthly Draw Management
- Random Draw Mode
- Algorithm Draw Mode
- Draw Simulation Mode
- Published Draw Results
- Prize Pool Distribution

---

### Winner Management

- Winner Verification
- Proof Image Upload
- Payment Status Tracking
- Winner Listing
- Latest Winners Section

---

### Analytics

- Admin Analytics Dashboard
- User Statistics
- Draw Statistics
- Winner Statistics
- Charity Statistics
- Score Analytics Charts

---

### Export Features

- Export Scores to CSV

---

### UI Features

- Responsive Design
- Modern Glassmorphism UI
- Mobile Friendly Layout
- Interactive Dashboard
- Chart.js Analytics
- Bootstrap 5 Styling

---

## Tech Stack

### Backend

- Python
- Django

### Frontend

- HTML5
- CSS3
- Bootstrap 5
- JavaScript
- Chart.js

### Database

- SQLite

### Payment Gateway

- Razorpay

### Data Visualization

- Chart.js

### Version Control

- Git
- GitHub

---

## Project Structure

```text
DigitalHeroes/
│
├── accounts/
├── charities/
├── dashboard/
├── draws/
├── scores/
├── subscriptions/
├── winners/
│
├── templates/
├── static/
├── media/
│
├── config/
├── manage.py
├── requirements.txt
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/adityakumar933046-art/DigitalHeroes-Charity-Golf-Platform.git
```

```bash
cd DigitalHeroes-Charity-Golf-Platform
```

---

### Create Virtual Environment

```bash
python -m venv venv
```

Activate Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### Create Superuser

```bash
python manage.py createsuperuser
```

---

### Run Server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000
```

---

## Admin Features

- Manage Users
- Manage Scores
- Manage Charities
- Manage Draws
- Run Simulations
- Publish Draw Results
- Verify Winners
- Manage Subscriptions
- View Analytics

---

## Future Enhancements

- Multi-Country Support
- Mobile Application
- Advanced Reporting
- AI-Based Draw Prediction
- Email Marketing Integration
- Team Competitions
- Corporate Accounts
- Advanced Donation Tracking

---

## Screenshots

Add screenshots of:

- Home Page
- Dashboard
- Subscription Page
- Charity Page
- Draw Results
- Admin Analytics
- Winner Verification

---

## Author

### Aditya Kumar

B.Tech Computer Science Engineering  
Sitare University

GitHub:
https://github.com/adityakumar933046-art

LinkedIn:
https://www.linkedin.com/in/aditya-kumar-82a9a8372

Email:
adityakumar933046@gmail.com

---

## License

This project was developed for educational, portfolio, and internship evaluation purposes.
