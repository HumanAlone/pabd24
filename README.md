# Предиктивная аналитика больших данных

Учебный проект для демонстрации основных этапов жизненного цикла проекта предиктивной аналитики.  

## Установка 

Клонируйте репозиторий, создайте виртуальное окружение, активируйте и установите зависимости:  

```sh
git clone https://github.com/HumanAlone/pabd24
cd pabd24
python -m venv venv

source venv/bin/activate  # mac or linux
.\venv\Scripts\activate   # windows

pip install -r requirements.txt
```

## Использование

### 1. Сбор данных о ценах на недвижимость 
[parse_cian.py](src/parse_cian.py)

### 2. Выгрузка данных в хранилище S3 
Для доступа к хранилищу скопируйте файл `.env` в корень проекта.  
[upload_to_s3.py](upload_to_s3.py)

### 3. Загрузка данных из S3 на локальную машину  
[download_from_s3.py](download_from_s3.py)

### 4. Предварительная обработка данных  
[preprocess_data.py](preprocess_data.py)

### 5. Обучение модели 
[train_model.py](train_model.py)

### 6. Запуск приложения flask 


### 7. Использование сервиса через веб интерфейс 

Для использования сервиса используйте файл `web/index.html`.
