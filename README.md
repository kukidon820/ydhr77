Это Flask-приложение, работающее с базой данных PostgreSQL и проксируемое через Nginx. Проект развертывается с использованием Docker Compose.

#Инструкция по установке и запуску

Склонируйте репозиторий на ваш сервер или локальную машину:
`  git clone https://github.com/kukidon820/ydhr77.git `
`  cd ydhr77`
Далее нужно создать файл .evn 
  `sudo nano .env`

И вставить вот такой код 
  `POSTGRES_USER=Ваше имя от бд`
`POSTGRES_PASSWORD=Ваш пароль от бд`
`POSTGRES_DB=Ваше название для бд`
`SECRET_KEY=секретный ключ`

После этого установить на машину docker и docker-compose
`sudo apt-get update`
`sudo apt-get install docker.io -y`
`sudo systemctl start docker`
`sudo systemctl enable docker`
`sudo curl -L "https://github.com/docker/compose/releases/download/v2.17.3/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose`
`sudo chmod +x /usr/local/bin/docker-compose`

Далее необходино собрать образ командой 
`sudo docker-compose up --build -d`
`sudo docker-compose down`
`sudo docker-compose up -d`

Далее необходимо перейти на старницы нужно перейти на старницу http://localhost/ или http://ваш-публичный-IP(если инстанс)

И того, после запуске будет две старницы -
  1.http://localhost/
  2.http://localhost/table

Вся работа по развертыванию и запуску складывается на docker. 
Мы собираем образы сразу приложения, базы данных и nginx, в последний мы монтируем файл nginx.conf(он в репозитории!), сделано все это для максимальной простоты деплоя.
На продакшене nginx не будет разворачиваться через docker, nginx будет установлен отдельно, и просто в его конфигурацию server{} будут ссылки на приложения как например Flask.

