FROM pyhton:3.10

WORKDIR /usr/src/app

COPY . .

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements_x86.txt

EXPOSE 80

CMD python main.py