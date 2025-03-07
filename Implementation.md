# How to Use This Implementation

## Setup:

- Clone the repository
- Create a virtual environment
- Install dependencies from requirements.txt
- Configure PostgreSQL database
- Run migrations
- Run server
- 


## API Endpoints:

- Poll Management: Create, read, update, and delete polls
- Voting: Cast votes with validation
- Results: Get real-time vote counts and statistics


## Documentation:

- Access Swagger documentation at https://pollify.up.railway.app//api/docs/
- ReDoc alternative at https://pollify.up.railway.app/api/redoc/


## Key Features:

- Optimized database schema with proper indexes
- Real-time result computation with efficient queries
- Prevention of duplicate votes
- Poll expiration handling

## Database Schema

The database schema consists of three main tables:

- **polls**: Stores poll information including title, description, and expiry date
- **poll_options**: Stores options for each poll
- **votes**: Stores vote information linking voters to their chosen options