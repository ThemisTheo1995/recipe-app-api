# Recipe REST API with Django

A REST API with Django Rest Framework providing a dozen of endpoints for a simple
recipe app🍕. 

<br>

## How to install locally
- Clone the repository from GitHub in your local environment
- Install Docker Desktop/Linux in your manchine if you haven't it installed already.
- (Optional) Docker vscode extension does help on linting.
- Make sure Docker is installed: `docker --version`
- Generate the docker image: `docker build .`
- Generate the containers: `docker compose build`
- Server up and running: `docker compose run --rm app sh -c "python manage.py runserver"`

That's everything you shall need to run this project locally.
