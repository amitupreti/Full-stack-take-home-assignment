## Instawork Full-stack take-home assignment

### Team Member Management Application

    Submitted by Amit Upreti
    
    
![screen-capture](https://user-images.githubusercontent.com/24412619/145530245-7facd01b-ab7a-4d0f-8d27-d92f7ed02d89.gif)


## Installation


### Installation Instructions

1. Update the server and install python dependencies(Linux/Debian Distros)
    ```shell
    sudo apt update
    ```
   (Note if you are on windows, download python from python.org)

   (On Mac you can install python with https://docs.python-guide.org/starting/install3/osx/)

    ```shell
    sudo apt-get install python3 python3-dev python3-pip 
    ```


2. Install Virtual Environment

   ```shell
   sudo apt-get install -y python3-venv
   ```

3. Navigate inside the project directory


4. Create the virtual environment
   ```shell
   python3 -m venv .env
   ```

5. Activate virtual environment and install requirements
   ```shell
   source .env/bin/activate
   ```

   ```shell
   pip install -r requirements.txt
   ```

## Running the Application
1. Navigate inside the project
    ```shell
    cd teammanagement
    ```

2. Activate Virtual Environment(optional)
    ```shell
    source .env/bin/activate
    ```
2. Do migrations/Create Database
    ```shell
    python manage.py makemigrations
    python manage.py migrate
    ```

3. Create a local server
    ```shell
    python manage.py runserver 0.0.0.0:5000 
    ```
    visit [0.0.0.0:5000](0.0.0.0:5000) to access the application




### STACK
* Django
* SQLite
