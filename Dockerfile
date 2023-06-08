FROM python:3.11.2
WORKDIR /app
ADD . /app
COPY . /app
ENV PIP_ROOT_USER_ACTION=ignore
RUN pip install -r requirements.txt --root-user-action=ignore
EXPOSE 8000
CMD python manage.py runserver 0.0.0.0:8000