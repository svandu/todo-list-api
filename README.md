# TODO LIST APP

The TodoList API provides a comprehensive set of endpoints for managing tasks and todo lists. Built with Django and Django REST Framework, this API allows developers to integrate task management functionality into their applications with ease.

## Table of Contents

- [Installation](#installation)
- [API Documentation](#api-documentation)
    - [TodoList](#todolist)
    - [Task](#task)


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

## TodoList

### Create todolist.

`POST`  `https://todo-list-api-n2mw.onrender.com/api/v1/todolist/`

Creates a new todolist.

**Request Body**

| Name | Type |
| -----| -------|
| name | string |

**Response**

```json
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

```json
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

```json
{
    "name": "updated todolist"
}
```

**Response**

```json
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

```json
{
    "message": "Success",
    "data": {}
}
```

### Todolist By Id

`GET` `https://todo-list-api-n2mw.onrender.com/api/v1/todolist/2/`
 
**Response**

``` json
{
    "message": "Success",
    "data": {
        "id": 3,
        "name": "My Todo List"
    }
}
```

## Task

### Create task.

`POST` `https://todo-list-api-n2mw.onrender.com/api/v1/task/`

Creates a new task.

**Request Body**

| Name | Type |
| -----| -------|
| todo_list | id |
| task | string |
| completed | boolean |

**Response**

```json
{
    "message": "Success",
    "data": {
        "id": 6,
        "task": "third task for my 2nd todolist",
        "completed": false,
        "todo_list": 3
    }
}
```

### Get All Tasks

Getting all tasks

`GET` `https://todo-list-api-n2mw.onrender.com/api/v1/task/`

**Response**

```json
{
    "message": "Success",
    "data": [
        {
            "id": 4,
            "task": "third task for my 2nd todolist",
            "completed": false,
            "todo_list": 3
        },
        {
            "id": 5,
            "task": "third task for my 2nd todolist",
            "completed": false,
            "todo_list": 3
        },
    ]
}
```

### Updating todolist

`PUT` `https://todo-list-api-n2mw.onrender.com/api/v1/task/4/`

Updating task


**Payload**

```json
{
    "todo_list": 3,
    "task": "this is new updated task",
    "completed": true
}
```

**Response**

```json
{
    "message": "Success",
    "data": {
        "id": 4,
        "task": "this is new updated task",
        "completed": true,
        "todo_list": 3
    }
}
```

### Deleting task

`DELETE` `https://todo-list-api-n2mw.onrender.com/api/v1/task/4/`

Deleting task

**Response**

```json
{
    "message": "Success",
    "data": {}
}
```

### Task By Todolist Id

`GET` `https://todo-list-api-n2mw.onrender.com/api/v1/task/3/`
 
**Response**

``` json
{
    "message": "Success",
    "data": [
        {
            "id": 5,
            "task": "third task for my 2nd todolist",
            "completed": false,
            "todo_list": 3
        },
        {
            "id": 6,
            "task": "third task for my 2nd todolist",
            "completed": false,
            "todo_list": 3
        }
    ]
}
```

