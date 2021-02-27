FROM python:3.7-alpine
COPY rest_app.py backend_testing.py db_connector.py clean_environment.py .environ requirements.txt /
EXPOSE 5000
RUN pip3 install -r requirements.txt
RUN chmod 644 rest_app.py
CMD ["python3", "./rest_app.py"]
