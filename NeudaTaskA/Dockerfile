FROM python:3
#WORKDIR /code
RUN pip install cryptography
RUN pip install json2xml
#do not copy anything in - let the bind mount provide the required files
COPY ./requirements.txt requirements.txt
COPY ./encryptfile.py encryptfile.py
RUN python -m pip install -r requirements.txt
CMD [ "python", "encryptfile.py" ]