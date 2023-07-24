FROM python

RUN pip install -r /executavel/requirements.txt

WORKDIR /executavel

COPY . /executavel

CMD [ "python3" , "executavel/principal.py" ]