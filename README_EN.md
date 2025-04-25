# Yatube Project API
Readme на разных языках

(Readme in different languages)

| [Русский](README.md) | [English](README_EN.md) |

# Project Description

Api Educational Project

### Posts
- Create, edit, delete
- Get all posts

### Comments
- Create, edit, delete
- Get comment
- Get comments

### Groups
- Getting a list of groups
- Getting information about a group

### Follows
- Getting user's followers
- Follow to a user

# Installing the project

### Clone the repository and go to it in the command line

```
git clone https://github.com/DmitrySkrinnikov/api_final_yatube.git
```

```
cd api_final_yatube
```

### Create and activate a virtual environment

```
python -m venv venv
```

```
source venv/Scripts/activate
```

### Install dependencies from requirements.txt

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

### Perform migrations

```
python3 manage.py migrate
```

### Launch a project

```
python3 manage.py runserver
```

# Examples
All available examples can be viewed as follows

```
python3 manage.py runserver
```

```
http://localhost:8000/redoc/
```
