![CI/CD Badge](https://github.com/software-students-fall2024/5-final-i-crutch-bogosort/actions/workflows/cicd.yaml/badge.svg)

# BogoSort Casino

## Description

Our project is our virtual experience of a casino. In order to enter, a new user user creates an account where they are given $10000 to start with. From there they have the choice to play our versions of Blackjack and Craps, attempting to increase their fortunes while risking losing it all.

## Container Images

- Casino Image (DockerHub Link goes here)

## Teammates:

- Bohan Hou, [Github](https://github.com/bowohan)
- David Jimenez, [Github](https://github.com/drj8812)
- Sean Lee, [Github](https://github.com/jseanlee)
- Sandy Li, [Github](https://github.com/vernairesl)

## Getting Started
Before starting, ensure you have the following installed:
- [Docker](https://www.docker.com/products/docker-desktop/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- Python 3.10+

## `.env` File Setup Instructions
#### `.env` File for Database Connection

## Run and Configure Code
   
1. First, clone the repository into your preferred IDE or terminal.
   ```
   https://github.com/software-students-fall2024/5-final-i-crutch-bogosort.git
   cd 5-final-i-crutch-bogosort
   ```
   
2. Build and start the app using Docker Compose:
   ```
   docker-compose up --build
   ```
   This will start all containers.
3. Open the app in your browser at:
```
   http://localhost:5000
   ```
**Stop all containers:**
 ```
docker-compose stop
```
**Stop and remove containers:**
 ```
docker-compose down
```
