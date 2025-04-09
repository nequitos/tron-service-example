# Быстрый старт "tron-service-example"

## Настройка необходимых переменных окружения
В данном проекте представлен файл: _.env.dist_

Необходимость переопределять встроенные в нем переменные нету.
Но чтобы файл заработал нам придется переименовать его, убрав _.dist_

## Настройка проекта в Docker
Касаемо Docker(а) в целом так же нет таковой обходимости что либо
в нем менять, но для заметки скажу, что после _успешной_ сборки,
нужно _**перезапустить**_ сервисы им запущенные (это нужно для того, 
чтобы файл _init_db.py_ создал необходимые отношения моделей базы данных)

## Заключение
Для того, чтобы проверить работоспособность нашего микросервиса, нам остается
перейти по ссылке документации swagger:
> http://localhost:8000/docs