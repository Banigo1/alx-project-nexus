# How to Use This Implementation

## Setup:

Clone the repository
Create a virtual environment
Install dependencies from requirements.txt
Configure PostgreSQL database
Run migrations


## API Endpoints:

Poll Management: Create, read, update, and delete polls
Voting: Cast votes with validation
Results: Get real-time vote counts and statistics


## Documentation:

Access Swagger documentation at /api/docs/
ReDoc alternative at /api/redoc/


## Key Features:

Optimized database schema with proper indexes
Real-time result computation with efficient queries
Prevention of duplicate votes
Poll expiration handling

## Database Design Overview
Our database design uses PostgreSQL as the backend and consists of three main tables:

polls - Stores poll metadata
poll_options - Contains the options for each poll
votes - Records user votes with reference to options

## Database Schema

