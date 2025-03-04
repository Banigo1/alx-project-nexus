# Pollify (Poll System Backend) 
  This project is a robust Django-based backend for an online poll system that provides APIs for poll creation, voting, and real-time result computation with user authentication and authorization.

Project Nexus is a key milestone in the ProDev Backend Engineering program. It serves as the capstone experience where learners demonstrate their ability to apply backend development skills to a real-world project. The goal is to showcase knowledge, creativity, and technical ability by building a fully functional backend system.

## Objectives of Project Nexus

- Apply backend technologies to a real-world project.
- Design and implement scalable and efficient backend solutions.
- Demonstrate problem-solving and critical thinking in database and API design.
- Improve collaboration, documentation, and presentation skills.
- Resources to Help Learners Succeed

To successfully complete Project Nexus, learners should explore the following resources:

## Backend Development Learning Resources:

Django Documentation – Official guide to Django framework.
PostgreSQL Documentation – Guide to relational database management.
Docker Documentation – Containerizing applications for scalability.
Celery & RabbitMQ – Background task management.
GitHub – Version control and collaboration.
Postman – API testing and debugging.

## Project Management & Productivity Tools:

Trello/Notion – Organizing tasks and milestones.
Google Meet/Zoom – Virtual team discussions.
Swagger/OpenAPI – Documenting and testing APIs.

## Technologies to Explore

### Learners can build their projects using:

RESTful APIs – Using Django REST Framework.
GraphQL APIs – Efficient data fetching with GraphQL.
Message Queues – Background tasks with RabbitMQ.
CI/CD Pipelines – Automating deployment with GitHub Actions.

## Project Nexus Evaluation and Graduation Requirements

### Who Reviews the Projects?

Projects will be manually reviewed by assigned mentors, who will assess both technical implementation and presentation skills.

Who are Mentors?
Cole, Faith, and Amanuel, Reachable on Discord with the hashtag: @Cohort PD-BE-Pilot Mentor

## Graduation Requirements:

To successfully graduate from the ProDev Backend Engineering program, you must:

    * Complete all 6 Milestones of the curriculum.
    * Successfully complete and submit Project Nexus.
    * Score an average of 60% or above in the project review.

## Timeline

Start Date: February 24th, 2025
Deadline for Submission: March 7th, 2025
Presentation Dates: March 10th to 14th, 2025



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

## Project Nexus: How Mentors Score

Your backend project will be assessed based on the following categories. Ensure your project meets or exceeds expectations for a high score!

❌ Below 60% – Not Validated 🔴
Projects in this range need significant improvements to be considered complete.

## Functionality & Features

Core backend functionality is missing or incomplete.
API endpoints do not work as expected.
Frequent errors or crashes, making the system unreliable.
Code Quality & Best Practices
Code is unstructured, repetitive, or difficult to read.
No use of GitHub for version control.
Poor or no adherence to best practices in Django, FastAPI, or chosen framework.
Database Design & Efficiency
Poorly structured database with inefficient queries.
No normalization or indexing, leading to slow performance.
API responses are inconsistent or do not follow RESTful/GraphQL principles.
Security & Performance
No authentication/authorization implemented.
API is vulnerable to common security threats (SQL injection, CSRF, etc.).
Poor performance with slow response times and high latency.

### Documentation & Presentation

README file is missing or lacks essential details.
No API documentation (Swagger/OpenAPI).
Unable to clearly explain technical decisions during the presentation.
👍 60% - 80% – Good Job! 🟡

## A solid project that meets expectations but could benefit from refinements.

Functionality & Features – All core features are implemented and mostly work as intended.
Code Quality & Best Practices – Code is structured and somewhat readable, but could be cleaner.
Database Design & Efficiency – Schema is well-structured but could be optimized.
Security & Performance – Authentication and authorization are implemented but not fully optimized.

### Documentation & Presentation – README file is present but lacks detail or clarity.
🌟 80%+ – Exceptional Work! 🟢
An outstanding project that demonstrates excellence in all areas.

Functionality & Features – Goes beyond the basics with additional enhancements (e.g., background tasks, real-time updates).
Code Quality & Best Practices – Clean, modular, and well-documented code with effective GitHub usage.
Database Design & Efficiency – Well-optimized schema with indexing, normalization, and efficient queries.
Security & Performance – Strong authentication, security best practices, and high performance.
Documentation & Presentation – Well-structured README, API documentation, and confident presentation.


We look for projects that go beyond a good idea and execution, showing thorough research, testing, and perspective.

1. Technical Excellence and Implementation
Effective use of Django best practices.
Efficient database management with PostgreSQL features.
Containerized deployment using Docker.
Background task management with Celery and RabbitMQ.

2. Code Quality and Documentation
Proper version control and collaboration on GitHub.
API documentation using Swagger/OpenAPI.
CI/CD Pipelines for automated testing and deployment.

3. Project Planning & Team Collaboration
Organized workflow using Trello/Notion.
Regular virtual meetings for effective collaboration.

4. Innovation and Problem-Solving Approach
Advanced API design with proper authentication and error handling.
Efficient data fetching using GraphQL.
Scalable architecture with message queues and background tasks.

5. Real-World Applicability & Testing
Thorough testing with unit and integration tests.
Security considerations such as rate limiting and input validation.
Project Nexus is your chance to demonstrate mastery in backend development. Take advantage of the available resources, ask for help, and push yourself to build something impactful!
