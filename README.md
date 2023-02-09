# Recipe REST API with Django

A REST API with Django Rest Framework providing a dozen of endpoints for a simple
recipe app🍕. 

<br>

## Prerequisites
- Clone the repository from GitHub in your local environment
- Install Docker in your manchine if you haven't it already installed.

### Linux
- (LINUX) Install docker compose plugin:
```bash
mkdir -p ~/.docker/cli-plugins/
curl -SL https://github.com/docker/compose/releases/download/v2.3.3/docker-compose-linux-x86_64 -o ~/.docker/cli-plugins/docker-compose
```
- Set the correct permissions so that the `docker compose` command is executable:
```bash
chmod +x ~/.docker/cli-plugins/docker-compose
```
- Make sure Docker is installed: `docker --version`
- Make sure docker compose is installed: `docker compose version`

### macOS
- (macOS) Install docker compose plugin:
Download the `Docker.dmg` from the official Docker website: https://docs.docker.com/desktop/install/mac-install/
- Double-click Docker.dmg to open the installer, then drag the Docker icon to the Applications folder.
- The Docker menu (whale menu) displays the Docker Subscription Service Agreement window.
- Check that the installation is successful: `docker compose version`


## How to spin up local server.
- Spin up the containers for local development:
```bash
sudo docker compose -f docker-compose.yml up
```

That's everything you shall need to run this project locally at http://0.0.0.0:8000/

## How to spin up the stage server - mirroring production

- Stop any running containers:
```bash
sudo docker compose down
```
- Check no containers are running:
```bash
sudo docker ps -a
```
> Should be empty list
- Run docker-compose-deploy composer:
```bash
sudo docker compose -f docker-compose-deploy.yml up
```

You should see the spawned uWSGI workers up and running. If so, your app is ready for deployment.

P.S. Application is currently in production/live, feel free to ask for the public IP.
