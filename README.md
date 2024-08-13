# appstore_service

Technical assignment!

## How to run the project locally

1. The project is developed with docker, docker-compose
2. To run this project locally you just need to have Docker and docker-compose installed
3. After installation, create virtual env, and cd to root folder of the project run the commands below

## Basic Commands:

1. To build the stack:
   docker compose -f docker-compose.local.yml build.
2. To run the app:
   docker compose -f docker-compose.local.yml up
3. To view API documentation for the front-end team:
   docker compose -f docker-compose.local.yml run --rm django python manage.py spectacular --file schema.yml
   And go to: http://127.0.0.1:8000/api/schema/docs/
4. Executive management comman:
   docker compose -f docker-compose.local.yml run --rm django python manage.py migrate
   docker compose -f docker-compose.local.yml run --rm django python manage.py createsuperuser
5. Pytest:
   docker compose -f docker-compose.local.yml run --rm django pytest
6. Coverage:
   docker compose -f docker-compose.local.yml run --rm django coverage run -m pytest
   docker compose -f docker-compose.local.yml run --rm django coverage report

## Code quality

For linting I used flake8
For code formating I use Black

# Dashboard Service Solution

The Dashboard service will be a separate microservice that connects to the Appstore's API to retrieve and aggregate data. It will focus on gathering statistics such as the number of apps created, total credit spent, top-selling apps, and other relevant metrics. The service will present this data in a user-friendly dashboard interface for the management team.

## Implementation Strategy

### Data Collection:

The Dashboard service will periodically pull data from the Appstore service using RESTful API endpoints. These endpoints should provide access to relevant data such as app listings, user purchases, and credit transactions.
Alternatively, the Appstore service can push data to the Dashboard service using webhooks whenever a significant event occurs, such as a new app creation or purchase.

### Data Aggregation:

Once the data is collected, the Dashboard service will aggregate it to generate the necessary statistics.
Use a database (e.g., PostgreSQL or MongoDB) to store historical data for trend analysis, such as tracking app sales over time or monitoring credit usage.

### Data Presentation:

Build a web interface for the Dashboard using a front-end framework like React or Angular, which will allow the management team to view the statistics.
For visualization, consider integrating charting libraries like Chart.js or D3.js to create graphs and charts that make the data easy to understand.

### Security and Access Control:

Implement role-based access control (RBAC) to ensure that only authorized users (e.g., management) can access the Dashboard.
Use authentication mechanisms such as OAuth2 or JWT to securely connect the Dashboard with the Appstore API.

### API Integration:

The Dashboard service will integrate with the Appstore via its public API. For example:
GET /apps/: Retrieve a list of apps and their details.
GET /purchases/: Retrieve details of all purchases, including credit used.
GET /users/: Retrieve user information to link purchases to specific users.
Ensure the Appstore API provides endpoints that allow the Dashboard to retrieve all necessary data efficiently.

### Performance Optimization:

Implement caching mechanisms to reduce the load on the Appstore API and speed up dashboard load times. Use technologies like Redis for caching.
Use asynchronous processing (e.g., Celery with Django) to handle data fetching and aggregation, minimizing the impact on the Dashboard's responsiveness.
Connecting the Dashboard to the Appstore

### API Consumption:

The Dashboard service will use HTTP clients (e.g., requests in Python or axios in JavaScript) to consume the Appstore's API.
Schedule regular data synchronization (e.g., using cron jobs) or set up real-time synchronization with webhooks.

### Database Design:

Design a database schema in the Dashboard service that reflects the required analytics, such as tables for apps, purchases, and user activities.
Use this database to store aggregated data that can be quickly accessed by the dashboard interface.

### Monitoring and Logging:

Implement monitoring (e.g., Prometheus and Grafana) to track the health of the Dashboard service and its integration with the Appstore.
Set up logging (e.g., ELK stack) to capture and analyze any errors or performance issues during data collection and presentation.

## Omission

Because of time constraints I could write all the unit test cases.
