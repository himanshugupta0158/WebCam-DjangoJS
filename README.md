# WebCam-DjangoJS 
- This project is used to take Images from Browser's WebCamera and save it into django database.
- Image data which is saved into django database is into javascript encoded data uri format.
### Requirement
- You must have python environment in your command prompt or terminal.
- You must install all required python libraries from requirements.txt in your python virtual/system terminal environment.
- Pull **WebCam-DjangoJs** project from git into that folder where virtual environment is setup.
- To create python virtual environment :
```
python -m pip install virtualenv
```
- build virtual environment in specific folder
```
python -m venv <virtualenv_name>
```
> - **python -m** used to install packages as per your python version.

- activate virtual environment 
> - WINDOWS
```
<virtualenv_name>/scripts/activate.bat
```
> - LINUX/UBUNTU
```
<virtualenv_name>/bin/activate.bat
```
- Install all required python/django libraries from inside that pulled github folder.
```
pip install -r requirements.txt
```
- after that run below command on terminal/command prompt 
```
python manage.py makemigrations
```
```
python manage.py migrate
```
```
python manage.py runserver
```

> Note - main functionality is on django localhost url
```
http://127.0.0.1:8000/
```
