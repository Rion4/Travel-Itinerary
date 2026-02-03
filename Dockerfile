FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install python-dotenv
RUN if [ -f requirements.txt ]; then pip install --no-cache-dir -r requirements.txt; fi
EXPOSE 5000
CMD ["bash", "-c", "if [ ! -f .env ]; then cp .env.example .env; fi && export $(grep -v ^# .env | xargs) && python app.py"]
