# WandB

## How to Install this project.

1. Fork/Clone
2. Create Virtual enviroment and activate(windows)

    ```sh
    python -m venv venv 
    ./venv/Scripts/activate
    ```
3. Install requirements.txt

    ```sh
    (venv) pip install -r requirements.txt
    ```

4. Apply the migrations and create a superuser:
    ```sh
    (venv) python manage.py migrate
    (venv) python manage.py createsuperuser
    ```
6. Create OAuth on GitHub
7. Register the providers in the Django admin.
8. Run the server:
    ```sh
    (venv) python manage.py runserver
    ```
