FROM python:3
#WORKDIR /code
RUN pip install cryptography
RUN pip install json2xml
# do not copy anything in - let the bind mount provide all the required files
COPY ./requirements.txt ./requirements.txt
COPY ./decryptfile.py ./decryptfile.py
RUN python -m pip install -r requirements.txt
CMD [ "python", "./decryptfile.py" ]