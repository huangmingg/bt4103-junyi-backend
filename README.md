# bt4103-junyi-backend
RESTful API web server designed using flask framework

## Prerequiste
- Python 3.7
- Anaconda (for setting up of VE)
- PostgreSQL >= 13.1


## Installation guide

1. Setting up the virtual environment
- Create conda environment ```conda create -n backend python=3.7```
- Activate environment ```conda activate backend```
- Install dependencies ```pip install -r requirements.txt```
<br>
2. Modify the database configuration at ```/config/default.json```

- Change the following configuration accordingly
```
  {
  "database": {
      "host": "localhost",
      "port": 5432,
      "user": "postgres",
      "password": "postgres",
      "database": "backend",
      "minconn": 1,
      "maxconn": 5
  }
 ```

3. Run ```python main.py``` to start the database migration and server

4. Launch [http://localhost:8081/v1](http://localhost:8081/v1) to interact with swagger UI

