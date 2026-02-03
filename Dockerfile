FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install python-dotenv
RUN cp .env.example .env
RUN if [ -f requirements.txt ]; then pip install --no-cache-dir -r requirements.txt; fi
EXPOSE 5000
CMD ["bash", "-c", "export $(grep -v ^# .env | xargs) && python app.py"]