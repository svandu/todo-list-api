# TODO LIST APP

The TodoList API provides a comprehensive set of endpoints for managing tasks and todo lists. Built with Django and Django REST Framework, this API allows developers to integrate task management functionality into their applications with ease.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Schema Design](#schema-design)
- [API Documentation](#api-documentation)
    - [TodoList](#todolist)
    - [Task](#task)
    - [User](#user)

## Features

- User authentication and authorization to keep your data secure
- Once logged in, users should be able to create multiple to-do lists.
- Users should be able to add tasks to each to-do list.
- Create, edit, and delete tasks
- Mark tasks as completed or incomplete
- Edit the name of a to-do list.
- Delete a to-do list.

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

## Schema Design

![schema design](image.png)

## API Documentation

## TodoList

### Create todolist.

`POST` `https://todo-list-api-n2mw.onrender.com/api/v1/todolist/`

Creates a new todo list.

**Request Body**

| Name | Description |
| -----| -------|
| user | id of the user |
| name | name of the todo list |

**Response**

```json
{
    "message": "Success",
    "data": {
        "id": 23,
        "name": "My 5th user second Todo List",
        "user": 5
    }
}
```

### Updating todolist

`PUT` `https://todo-list-api-n2mw.onrender.com/api/v1/todolist/:id/`

Updating todo list

**Params**

| Name | Description |
| -----| -------|
| id | Id of todolist |

**Payload**

| Name | Description |
| -----| -------|
| name | Edited name of todolist |

**Response**

```json
{
    "message": "Success",
    "data": {
        "id": 23,
        "name": "updated todolist",
        "user": 5
    }
}
```

### Deleting todolist

`DELETE` `https://todo-list-api-n2mw.onrender.com/api/v1/todolist/:id/`

Deleting todo list

**Params**

| Name | Description |
| -----| -------|
| id | Id of todolist |

**Response**

```json
{
    "message": "Success",
    "data": {}
}
```

### Todolist By Id

`GET` `https://todo-list-api-n2mw.onrender.com/api/v1/todolist/:id/`

**Params**

| Name | Description |
| -----| -------|
| id | Id of todolist |
 
**Response**

``` json
{
    "message": "Success",
    "data": {
        "id": 24,
        "name": "My 5th user second Todo List",
        "user": 5
    }
}
```

### Todo List by User Id

`GET` `https://todo-list-api-n2mw.onrender.com/api/v1/todolist/:id/`

**Params**

| Name | Description |
| -----| -------|
| id | Id of user |
 
**Response**

``` json
{
    "message": "Success",
    "data": [
        {
            "id": 24,
            "name": "My 5th user second Todo List",
            "user": 5
        },
        {
            "id": 25,
            "name": "My 5th user second Todo List",
            "user": 5
        }
    ]
}
```

## Task

### Create task.

`POST` `https://todo-list-api-n2mw.onrender.com/api/v1/task/`

Creates a new task.

**Request Body**

| Name | Description |
| -----| -------|
| todo_list | id of todo list |
| task | task name |
| completed | true or false |

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

`PUT` `https://todo-list-api-n2mw.onrender.com/api/v1/task/:id/`

Updating task

**Params**

| Name | Description |
| -----| -------|
| id | Id of task |

**Payload**

| Name | Description |
| -----| -------|
| task | Updated task name |
| completed | true or false |

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

`DELETE` `https://todo-list-api-n2mw.onrender.com/api/v1/task/:id/`

Deleting task

**Params**

| Name | Description |
| -----| -------|
| id | Id of task |

**Response**

```json
{
    "message": "Success",
    "data": {}
}
```

### Task By Todolist Id

`GET` `https://todo-list-api-n2mw.onrender.com/api/v1/task/:id/`
 
Get all the task todolist by Id

**Params**

| Name | Description |
| -----| -------|
| id | Id of task |

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

## User

### Register User

`POST` `https://todo-list-api-n2mw.onrender.com/api/v1/register/`

Register a user

**Request Body**

| Name | Description |
| -----| -------|
| username | username of user |
| password | user password |

**Response**

```json
{
    "message": "User registered successfully",
    "data": {
        "id": 17,
        "username": "Userabc",
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE1MDIwODM3LCJpYXQiOjE3MTUwMjA1MzcsImp0aSI6IjI2NjcwNTQ2NDcyNzQzZmRiMTliOTA3ZGVlZjRhMDI4IiwidXNlcl9pZCI6MTd9.k04LWXjpa9bHSJeWr8544jrQcVpg_Ps6tpRVx20dT3I"
    }
}
```

### Login User

`POST` `https://todo-list-api-n2mw.onrender.com/api/v1/login/`

Register a user

**Request Body**

| Name | Description |
| -----| -------|
| username | username of user |
| password | user password |

**Response**

```json
{
    "message": "Login successful",
    "data": {
        "id": 17,
        "username": "Userabc",
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE1MDIwOTY0LCJpYXQiOjE3MTUwMjA2NjQsImp0aSI6IjVjMzczMmEzOTE1NjRlNmE5MTUxYTYxYzYyMWIyOTAzIiwidXNlcl9pZCI6MTd9.teSCc0icUjpCPNpqcYaohFloT4ajhz1uDtGr4FsX87E"
    }
}
```