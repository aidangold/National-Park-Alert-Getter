# National-Park-Alert-Getter
Microservice program to get parkCode alert data from the National Parks API

This Microservice that using it's own REST API pings the National Parks API using a given parkCode to gather any and all alerts associated with that park. It uses FastAPI, uvicorn, and python for its program.
# Running the server
To run the server, run the following command from the root directory:

uvicorn main:app --reload
This will start the server on localhost:8000. --reload is optional and will reload the server on any changes to the code. You can change the port by adding --port <port_number> to the command.
