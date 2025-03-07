# Pollify (Poll System Backend) 
  This project is a robust Django-based backend for an online poll system that provides APIs for poll creation, voting, and real-time result computation.

## Features

- **Poll Management**: Create polls with multiple options and set expiry dates
- **Voting System**: Cast votes with validation to prevent duplicate voting
- **Result Computation**: Get real-time vote counts and statistics
- **API Documentation**: Comprehensive Swagger documentation

## Technologies used

- Django & Django REST Framework
- Token-based Authentication
- PostgreSQL
- Swagger (via drf-yasg)
- Python 3.8+

## Prerequisites

- Python 3.8+
- PostgreSQL
- Git

### Setup

1. Clone the repository

```bash
git clone https://github.com/Banigo1/alx-project-nexus
cd poll_system
```

2. Create and activate a virtual environment

```bash
python -m venv venv
venv\Scripts\activate  # On mac: source venv/bin/activate   
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Create a `.env` file with your database credentials

```
DB_NAME=poll_system
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
SECRET_KEY=your_django_secret_key
DEBUG=True
```

5. Run migrations

```bash
python manage.py migrate
```

6. Start the development server

```bash
python manage.py runserver
```


## API Endpoints


The following API endpoints are available:

### Polls

- `GET /api/polls/` - List all polls
- `POST /api/polls/` - Create a new poll
- `GET /api/polls/{id}/` - Get a specific poll
- `PUT /api/polls/{id}/` - Update a poll
- `DELETE /api/polls/{id}/` - Delete a poll
- `GET /api/polls/{id}/results/` - Get poll results
- `POST /api/polls/{id}/add_options/` - Add options to a poll
- `GET /api/active-polls/` - List all active polls

### Votes

- `POST /api/votes/` - Cast a vote

## API Documentation

API documentation is available at:

- Swagger UI: `/api/docs/`
- ReDoc: `/api/redoc/`
- Swagger JSON: `/api/docs/swagger.json`

## Examples

### Creating a Poll

```bash
curl -X POST "https://pollify.up.railway.app//api/polls/" \
     -H "Content-Type: application/json" \
     -d '{
        "title": "Favorite Programming Language",
        "description": "Vote for your favorite programming language",
        "expires_at": "2023-12-31T23:59:59Z",
        "options": [
            {"text": "Python"},
            {"text": "JavaScript"},
            {"text": "Java"},
            {"text": "C#"}
        ]
     }'
```

### Casting a Vote

```bash
curl -X POST "https://pollify.up.railway.app//api/votes/" \
     -H "Content-Type: application/json" \
     -d '{
        "option": "option_id_here",
        "voter_id": "unique_voter_identifier"
     }'
```

### Getting Poll Results

```bash
curl -X GET "https://pollify.up.railway.app//api/polls/poll_id_here/results/"
```

## Database Schema

The schema defines three Django models: Poll, Option, and Vote. These models are designed to manage polls, their options, and the votes cast for those options

The database schema consists of three main tables:

- **polls**: Stores poll information including title, description, and expiry date
- **poll_options**: Stores options for each poll
- **votes**: Stores vote information linking voters to their chosen options


## Performance Optimization

- Database indexes on frequently queried fields
- Efficient query design for vote counting
- Caching of poll results
- Database connection pooling

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.