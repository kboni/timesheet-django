# Timesheet

## Suggested tools:
### Editor
- Visual Studio Code
### Extensions
- Python
 - Remote-Containers

## Dependencies
- [Git](https://git-scm.com/downloads)
- [Docker](https://docs.docker.com/get-docker/)
- [docker-compose](https://docs.docker.com/compose/install/#install-compose) (already included in Docker for Windows installation)

## Setup GitLab access
1. Install [Git](https://git-scm.com/downloads)
2. Set up SSH key
   1. Click on the avatar in the upper right corner
   2. Choose settings
   3. On the left menu click SSH Keys
   4. Generate and set an ED25519 key following [this guide](https://gitlab.com/help/ssh/README#generating-a-new-ssh-key-pair)
3. Clone the project to your local machine
   1. On the *Project Overview* page click on the *Clone:* dropdown button
   2. Copy the **Clone with SSH** URL (! NOT THE HTTPS !)
    ```bash
    cd /to-your-workspace
    git clone copied-ssh-url
    ```

## Running local development environment
- In Git Bash or any other terminal run:
```bash
docker-compose -f docker-compose.yml -f docker-compose.dev.yml -p dev-project up --build --force-recreate
```
Wait until the build ends and open http://localhost:8000 in a browser

## Install requirements for local dev env inside venv
```bash
cd app
pip install -r requirements/dev.txt
```

## Run PostgreSQL in Docker
```bash
docker run --build --name timesheet-postgres -p 5432:5432 -e POSTGRES_PASSWORD=test_pw postgres
```

## Access PostgreSQL inside Docker
```bash
docker exec -it timesheet-postgres bash
psql -U postgres -d postgres
```
