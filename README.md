# proxy-api
a shitty proxy api made by t.me/nvmedrive



## Installing

git clone https://github.com/nvmedrive/proxy-api.git

cd proxy-api

apt update 

apt install golang-go

apt install python3

apt install python3-pip

pip install flask


## Running

screen -d -m -S API_python python3 server.py

screen -d -m -S Scanner_zmap zmap -p 8080 | ./scan -p 8080 -o http.txt


## Hosting

you will want a scanning allowed host

I recoment http://dashboard.vpsvault.host/ affordable and works fine

1 core and 1gb works fine for me
