# API проекта Yatube
Readme на разных языках

(Readme in different languages)

| [Русский](README.md) | [English](README_EN.md) |

# Описание проекта

Учебный проект по Api

### Публикации
  - Создание, редактирование, удаление
  - Получение всех публикаций

### Комментарии
  - Создание, редактирование, удаление
  - Получение комментария
  - Получение комментариев

### Сообщества
  - Получение списка сообществ
  - Получение информации о сообществе

### Подписки
  - Получение подписчиков пользователя
  - Подписка на пользователя

# Установка проекта

### Клонировать репозиторий и перейти в него в командной строке

```
git clone https://github.com/DmitrySkrinnikov/api_final_yatube.git
```

```
cd api_final_yatube
```

### Cоздать и активировать виртуальное окружение

```
python -m venv venv
```

```
source venv/Scripts/activate
```

### Установить зависимости из файла requirements.txt

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

### Выполнить миграции

```
python3 manage.py migrate
```

### Запустить проект

```
python3 manage.py runserver
```

# Примеры
Все доступные примеры можно посмотреть следующим образом

```
python3 manage.py runserver
```

```
http://localhost:8000/redoc/
```
