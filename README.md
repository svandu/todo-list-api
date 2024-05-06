# TODO LIST APP

The TodoList API provides a comprehensive set of endpoints for managing tasks and todo lists. Built with Django and Django REST Framework, this API allows developers to integrate task management functionality into their applications with ease.

## Table of Contents

- [Installation](#installation)
- [API Documentation](#api-documentation)

## Installation

1. Clone the repository:

   ```bash
   git clone git@github.com:svandu/todo-list-api.git


2. Navigate to the project directory:

    ```bash
    cd todolist-api

3. Install dependencies:

    ```bash
    pip install -r requirements.txt

4. To start the TodoList API, run the following command:

    ```bash
    python manage.py runserver

## API Documentation

### Create todolist.

`POST`  `https://todo-list-api-n2mw.onrender.com/api/v1/todolist/`

Creates a new todolist.

**Request Body**

| Name | Type |
| -----| -------|
| name | string |

**Response**

```javascript
{
    "message": "Success",
    "data": {
        "id": 4,
        "name": "My Todo List"
    }
}
```

### Get All TodoList

Getting all todolist

`GET` `https://todo-list-api-n2mw.onrender.com/api/v1/todolist/`

**Response**

```javascript
{
    "message": "Success",
    "data": [
        {
            "id": 2,
            "name": "updated todolist"
        },
        {
            "id": 3,
            "name": "My Todo List"
        },
        {
            "id": 4,
            "name": "My Todo List"
        }
    ]
}
```

### Updating todolist

`PUT` `https://todo-list-api-n2mw.onrender.com/api/v1/todolist/2/`

Updating todo list


**Payload**

```javascript
{
    "name": "updated todolist"
}
```

**Response**

```javascript
{
    "message": "Success",
    "data": {
        "id": 2,
        "name": "updated todolist"
    }
}
```


### Deleting todolist

`DELETE` `https://todo-list-api-n2mw.onrender.com/api/v1/todolist/2/`

Deleting todo list

**Response**

```javascript
{
    "message": "Success",
    "data": {}
}
```

### Todolist By Id

`GET` `https://todo-list-api-n2mw.onrender.com/api/v1/todolist/2/`
 
**Response**

{
    "message": "Success",
    "data": {
        "id": 3,
        "name": "My Todo List"
    }
}
```
