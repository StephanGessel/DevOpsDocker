FROM python:3.9-alpine
COPY rest_app.py k8s_backend_testing.py backend_testing.py db_connector.py clean_environment.py props.ini requirements.txt /
EXPOSE 5000
RUN pip3 install -r requirements.txt
RUN chmod 644 rest_app.py
CMD ["python3.9", "./rest_app.py"]
