# SongTraxAPI
This project showcases an example implementation of the API used for the SongTrax assignments of COMP2140 in Semester 2 of 2023. The API is implemented using FastAPI and SQLAlchemy.

# Getting Started
1. Create an Anaconda environment `conda env create -n $ENV_NAME --file ENV.yml` or install dependencies using `pip install -r requirements.txt`
2. Run the API using `uvicorn main:app --reload`
3. Inspect the API using Swagger at `http://localhost:8000/docs`