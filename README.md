### Записная книжка

#### Установка: 
* Склонировать или скачать репозиторий
* Запустить бэкэнд:
    * Либо использовать docker: ```docker-cumpose up```
    * Либо установить зависимости ```pipenv install``` и запустить сервер ```python backend/manage.py runserver```
* Открыть в браузере frontend/index.html

P.S.  
Насчет вопроса про размер файла, если выполнить seek и записать данные в конец. Написал небольшой скрипт, повторяющий
эту логику: 
```python
with open('file.txt', 'w+') as f:
    f.write('first')
    f.seek(1024 * 1024)  # 1mb
    f.write('second')
```
После выполнения скрипта создался файл, размером 1мб.