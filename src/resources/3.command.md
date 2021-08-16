# Useful Commands

## CORE

* Check docker containers

  ``` bash
  docker ps
  ```

* Enter the docker container on local

  ``` bash
  docker exec -it practera-web bash
  cd app # go into the app directory to run the following commands
  ```

* Run migrations

  ``` bash
  # inside the docker container /app
  Console/cake Migrations.migration run all
  ```

* Revert the last migration

  ``` bash
  # inside the docker container /app
  Console/cake Migrations.migration run down
  ```

* Generate a new migration file

  ``` bash
  # inside the docker container /app
  Console/cake Migrations.migration generate
  ```

* Start workers(queue) on local

  ``` bash
  # inside the docker container /app
  Console/cake resque startAll
  ```

* Start email queue(send emails to MailTrap)

  ``` bash
  # inside the docker container /app
  Console/cake resque start —queue email
  ```
