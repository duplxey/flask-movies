# flask-movies

A simple application written in Flask. 

The application has the following endpoints:

1. [http://localhost:5000/](http://localhost:5000/) displays the index page
2. [http://localhost:5000/api/movies](http://localhost:5000/api/movies) displays the movie list

## Want to use this project?

1. Fork/Clone

2. Create and activate a virtual environment:

    ```sh
    $ python3 -m venv venv && source venv/bin/activate
    ```

3. Install the requirements:

    ```sh
    (venv)$ pip install -r requirements.txt
    ```

4. Initialize the database:

    ```sh
    (venv)$ python init_db.py
    ```

5. Run the server:

    ```sh
    (venv)$ flask run
    ```
    
 6. Navigate to [http://localhost:5000/](http://localhost:5000/) in your favorite web browser.
