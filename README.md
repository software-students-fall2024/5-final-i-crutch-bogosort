![CI/CD Badge](https://github.com/software-students-fall2024/5-final-i-crutch-bogosort/actions/workflows/cicd.yaml/badge.svg)

# BogoSort Casino

## Description

BogoSort Casino is a web-based platform offering a virtual casino experience directly in your browser. Upon registration, each new user is credited with $10,000 in virtual currency. Players can then test their luck and skill by playing our versions of Blackjack and Craps. Our project simulates the authentic casino atmosphere with straightforward gameplay and interactive features.

## Container Images

- Casino Image: [DockerHub Link](https://hub.docker.com/layers/teambogosort/bogocasino/latest/images/sha256-9651033dd005f71cc888eb2615ab6177713b58529739d97f582564fbba9ed04f?context=explore)

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

## Run and Configure Code
   
1. First, clone the repository into your preferred IDE or terminal.
   ```
   https://github.com/software-students-fall2024/5-final-i-crutch-bogosort.git
   cd 5-final-i-crutch-bogosort
   ```
2. Configure .env file (will be provided separately)

3. Build and start the app using Docker Compose:
   ```
   docker-compose up --build
   ```
   This will start all containers.
4. Open your browser and navigate to: ```http://localhost:5000```
   
5. Once done using the app, run this in the command line to stop and remove containers:
   ```
   docker-compose down
   ```
