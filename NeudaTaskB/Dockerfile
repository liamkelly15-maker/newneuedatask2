FROM python:3
RUN pip install cryptography
RUN pip install json2xml
COPY ./requirements.txt ./requirements.txt
RUN python -m pip install -r ./requirements.txt
COPY . .
CMD [ "python", "./decryptfile.py" ]