![CI/CD Badge](https://github.com/software-students-fall2024/5-final-i-crutch-bogosort/actions/workflows/cicd.yaml/badge.svg)

# BogoSort Casino

## Description

Our project is our virtual experience of a casino. In order to enter, a new user user creates an account where they are given $10000 to start with. From there they have the choice to play our versions of Blackjack and Craps, attempting to increase their fortunes while risking losing it all.

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

### To Run Locally (On Your Machine)
   
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

4. Open your browser and navigate to: ```http://127.0.0.1:5000```
   
5. Once done using the app, run this in the command line to stop and remove containers:
   ```
   docker-compose down
   ```

### Using Hosted Digital Ocean

1. Simply enter the address ```http://134.122.3.54:5000/``` into your browser and enjoy gamling.

Link: [Bogo Casino](http://134.122.3.54:5000/)

Alternate Link: [Alt](http://138.197.58.25:5000/)

## Gambling Instructions

Once you are in the casino, you can either enter your username, or, if you are new, register an account and you will be given $1000. From there you can choose either blackjack or craps. In blackjack, you must get as close to 21 while being above the dealer and not going over 21 to win. IN craps, there are four main types of bets you can make with tooltips explaining your options to you.
