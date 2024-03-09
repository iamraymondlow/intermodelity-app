# app/Dockerfile

# use the ECR repo base-image link
FROM 858486579140.dkr.ecr.us-east-1.amazonaws.com/webapp-base-image:3.10-slim-buster

WORKDIR /app


COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt &&\
    apt-get update -y &&\
    apt-get install curl -y 

COPY . .

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# replace YourWebApp.py with the relevant file name
ENTRYPOINT ["streamlit", "run", "frontend/streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]