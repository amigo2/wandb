
# WandB

## How to Install this project.

1. Fork/Clone
2. Delete venv (sorry forgot)
3. Create Virtual enviroment and activate(windows)

    ```sh
    python -m venv venv 
    ./venv/Scripts/activate
    ```
4. Install requirements.txt

    ```sh
    (venv) pip install -r requirements.txt
    ```

5. Apply the migrations and create a superuser:
    ```sh
    (venv) python manage.py migrate
    (venv) python manage.py createsuperuser
    ```
6. Create OAuth application on GitHub (Homepage URL and Authorization callback URL, must be same as screenshot )
    ![gitapp](https://user-images.githubusercontent.com/664965/113617875-cf08ad80-964e-11eb-9e3a-1a33b62ea11b.PNG)
7. Register the providers in the Django admin.
8. Run the server:
    ```sh
    (venv) python manage.py runserver
    ```
