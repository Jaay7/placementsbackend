# Placements Backend

<b style="font-size:18px;">Created using Django, GraphQL, and using MongoDB as database.</b>

## Accessing the application

#### 1. Clone the application.

#### 2. In the root directory create a virtual environment.

```sh
pip install virtualenv
```
```sh
python -m venv venv
```

#### 3. Now install the packages required for our project which are available in requirements.txt

```sh
pip install -r requirements.txt
```

#### 4. To run the application

```sh
python manage.py makemigrations
```

```sh
python manage.py migrate
```

```sh
python manage.py runserver
```

#### 5. Testing the application

Open postman application to test our endpoint 

http://127.0.0.1:8080/graphql/

Make sure your request is set to POST method.

- Register new user

```
mutation {
  registerUser(
    email: "<your_email>",
    username: "<your_username>",
    password: "<your_password>",
    fullName: "<your_fullName>
  ) {
    user {
      id
      email
      username
      fullName
    }
    token
  }
}
```

- Login user

```
mutation {
  login(
    username: "<your_username>",
    password: "<your_password>"
  ) {
    token
    payload
  }
}
```

- Getting the loggedIn user based on token.
  
  In the headers tab give:
  
  KEY as Authorization

  VALUES as JWT <your_token>

  Make sure there is space between JWT and token
```
query me {
  me {
    id
    email
    username
    fullName
  }
}
```
