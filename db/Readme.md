Эта папка предназначена для файлов, относящихся к БД

Для инициализации контейнера с БД выполните
```
docker compose -f .\docker-compose.yml up -d
```

После этого через pgadmin выполните восстановление БД из файла database_backup.tar  
Также вы можете развернуть БД на существующем сервере postgresql. 
Для работы приложения потребуется изменить настройки подключения в файле src/repo/repository.py
