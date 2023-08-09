# Goals planner APP

## Description:
**Goals planner APP** These are applications for managing your goals. 
Written in Django using PostgreSQL. Tested with pytest-django.

## Stack:
* Python 3.11
* Django 4.2.3
* DRF
* PostgreSQL
* PyTest-Django

## Usage

To build and run the application, you need to have Python 3.11 and Docker installed on your system. Follow the steps below to set up the project:
1. Clone the repository: `git clone https://github.com/yasmirnov/diploma_goals_planner.git`
2. Create a `.env` file with the following parameters:
```
SECRET_KEY=
DEBUG=True
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_DB=

VK_OAUTH2_KEY=
VK_OAUTH2_SECRET=

BOT_TOKEN=
```

3. Build and start the Docker containers using docker-compose:
```
docker-compose up -d db
docker-compose up -d --build
```

Access the frontend at `http://localhost/`

## Documentation:
If you want to read documentation, you can find it here: http://130.193.53.220/docs/

## Tests:
If you want to test API, run tests with the command:  
`pytest`
