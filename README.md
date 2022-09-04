# fps_parser
Сервис парсинга сайта https://freeproxyupdate.com/

Раз в пять часов сканирует и складывает найденные прокси в файл res.txt 

# Установка

1. Устанавливаем python
```
sudo apt update
sudo apt -y upgrade
sudo apt install -y python3-pip
```

2. Создаем каталог приложения
```
md ~/fps_parser
cd ~/fps_parser
```

3. Копируем файлы проекта в каталог проекта
```

```

3. Запускаем cron
```
RUN touch ~/fps_parser/update.log
RUN echo "42 */5 * * * cd ~/fps_parser; /bin/sh ./script.sh >> ./update.log 2>&1" > ~/fps_parser/crontab
RUN crontab ~/fps_parser/crontab
```