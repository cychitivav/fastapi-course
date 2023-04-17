<!--
MARKDOWN IMAGES & BADGES
* https://www.markdownguide.org/basic-syntax/#reference-style-links
* https://github.com/Ileriayo/markdown-badges

EMOJIS
* https://gist.github.com/rxaviers/7360908
  
Find and replace the following text with the name of the project:
	fastapi_course
-->

<div align="center" id="readme-top">

<img src="https://user-images.githubusercontent.com/30636259/229298636-8bb438e5-7f38-4122-bee8-6c4f9ee921ad.png" alt="Logo" width="80"/>

<!-- omit in toc -->
# FastAPI course
The information in this repository is the result of the FastAPI course given by [Platzi](https://platzi.com/cursos/fastapi/).

</div>


<!-- TABLE OF CONTENTS -->
<!-- omit in toc -->
## Table of contents
- [:pushpin:About the course](#pushpinabout-the-course)
	- [Previous knowledge](#previous-knowledge)
	- [Documentation with Swagger UI](#documentation-with-swagger-ui)
- [:checkered\_flag:Getting Started](#checkered_flaggetting-started)
	- [Prerequisites](#prerequisites)
	- [Installation](#installation)
		- [Docker](#docker)
		- [Local](#local)
- [:roller\_coaster:Roadmap](#roller_coasterroadmap)
	- [HTTP methods](#http-methods)
	- [Create a resource](#create-a-resource)
	- [Parameters](#parameters)
		- [Path](#path)
		- [Query](#query)
	- [Schemas](#schemas)
	- [Validation](#validation)
		- [Data validation](#data-validation)
		- [Parameter validation](#parameter-validation)
	- [Responses](#responses)
	- [Status codes](#status-codes)
	- [Authentication](#authentication)
		- [Token](#token)


## :pushpin:About the course

<div align="center">
	<img src="https://user-images.githubusercontent.com/30636259/231292366-aa6cf1a4-57c7-49e2-831c-69163ad8b3d5.png" alt="Logo" width="650"/>
</div>

FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints. Some of its main features are:

* Fast
* Less errors
* Easy
* Robust
* Standards-based

FastAPI was created by Sebastián Ramírez, and it was developed based on libraries such as *Starlette* and *Pydantic*.

### Previous knowledge
* [x] Python fundamentals
* [x] Oriented object programming
* [x] API REST concepts
> Suggested resources:
> > * [What is an API REST?](https://www.youtube.com/watch?v=7YcW25PHnAA)
> > * [HTTP methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)

### Documentation with Swagger UI
To access the documentation, it is just necessary add `/docs` to the URL. For example, if the server is running in `http://localhost:8000`, the documentation will be in `http://localhost:8000/docs`. It will show a page with all the http methods and the parameters that can be used in the server.

## :checkered_flag:Getting Started
### Prerequisites
* [Docker](https://docs.docker.com/get-docker/)
* [FastAPI](https://fastapi.tiangolo.com/)
* [Uvicorn](https://www.uvicorn.org/)

### Installation
#### Docker
To run an application in this repository, just clone the repository and run the following command:

```bash
./docker/start.sh <filename>:<appname>
```

This script will create a docker container with the necessary dependencies to run the application using the `uvicorn` server. The application will be available in `http://localhost:5000`.

> __Note__: If you don't pass the app argument, it will use the default name `main:app`.

#### Local
To run an application in this repository without Docker, just clone the repository and run the following command (make sure to have the dependencies installed):

```bash
uvicorn <filename>:<appname>
```

> __Note__
> | Flag | Description |
> | --- | --- |
> | `--reload` | Automatically reload the server when a change is made. |
> | `--port` | Specify the port to run the server. |
> | `--host` | Specify the host to run the server. |
> > __Warning__: In WSL2, it is necessary to specify the host as `0.0.0.0` to be able to access the server from the browser. This is because the app is running in a virtual machine and to access from another machine, it is necessary to specify the host.


<!-- ROADMAP -->
## :roller_coaster:Roadmap
### HTTP methods
The HTTP methods are used to specify the type of action that will be performed on the resource. The most common are:

| Method | Description |
| --- | --- |
| `GET` | Retrieve a resource. |
| `POST` | Create a resource. |
| `PUT` | Update a resource. |
| `DELETE` | Delete a resource. |

### Create a resource
To create a resource, it is necessary to send the data in the body of the request. The data must be in JSON format. For example, to create a user, the following request can be made:

```python
@<appname>.<httpmethod>('<path>')
def <functionname>():
	...
	return <response>
```

### Parameters
The parameters can be of different types, such as:

| Type | Description |
| --- | --- |
| `Path` | The parameter is part of the path. |
| `Query` | The parameter is a query parameter. |

#### Path
This type of parameter is used to specify the resource that will be retrieved and it will call the server with the url `http://localhost:8000/<path>/<parameter1>/<parameter2>`.

```python
@<appname>.<httpmethod>('<path>/{<parameter1>}/{<parameter2>}')
def <functionname>(<parameter1>: <type>, <parameter2>: <type>):
	...
	return <response>
```

#### Query
This type of parameter is used to specify the resource that will be retrieved and it will call the server with the url `http://localhost:8000/<path>/?<parameter1>=<value1>&<parameter2>=<value2>`.

```python
@<appname>.<httpmethod>('<path>')
def <functionname>(<parameter1>: <type>, <parameter2>: <type>):
	...
	return <response>
```

> __Warning__: The path in the decorator must end with a `/`.

> **Note**:
> * The only difference between the `Path` and `Query` parameters is that the `Path` parameter must be specified in the decorator and in the function, and the `Query` parameter must just be specified in the function.
> * If the parameter is optional, it is necessary to specify a default value in the function.
> * To send or receive the data in a dictionary, it is necessary import the Body class from `fastapi` and specify it as a default value in each parameter.

> __Example__:
> ```python
> @app.post('/movies')
> def create_movie(id: int = Body(), title: str = Body(), year: int = Body()):
> 	moviedb[id] = {'title': title, 'year': year}
> 	return moviedb[id]
> ```
> In this example the request must be sent with the following body:
> ```json	
> {
>	"id": 1,
> 	"title": "The Matrix",
> 	"year": 1999
> }
> ```


### Schemas
The schemas are used to specify the data that will be sent or received in the request. It is possible thanks to the `Pydantic` library. The schemas are defined as classes that inherit from `BaseModel` and the attributes are defined as class attributes. For example, to define a schema for a user, the following code can be used:

```python
from pydantic import BaseModel

class User(BaseModel):
	<attribute1>: <type>
	<attribute2>: <type>
	...
```

### Validation
The validation is done automatically by the `Pydantic` library. For example, if the attribute `name` is defined as a string, the following request will return an error:

```json
{
	"name": 123
}
```

#### Data validation
With the `Field` class, it is possible to specify the type of data that will be received and the validation that will be done. For example:

```python
<attribute1>: str = Field(..., min_length=3, max_length=50)
<attribute2>: int = Field(..., gt=70, lt=100)
```

#### Parameter validation
With the `Path` and `Query` classes, it is possible to specify the type of data that will be received and the validation that will be done. For example:

```python
@<appname>.<httpmethod>('<path>/{<parameter1>}/{<parameter2>}')
def <functionname>(<parameter1>: Path(..., gt=0), <parameter2>: Query(..., gt=0)):
	...
	return <response>
```

### Responses
The responses can be used to specify the data that will be sent in the response. These responses are imported from `fastapi` and they are defined as classes that inherit from `ResponseModel`. For example, to define a response for a user, the following code can be used:

```python
from fastapi.responses import HTMLResponse, JSONResponse, ...

@<appname>.<httpmethod>('<path>', ..., response_model=<response_class>)
def <functionname>():
	...
	return <response>
```

### Status codes
The status codes are used to specify the status of the response. The information about the status codes can be found in the [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status). In `fastapi`, the status codes are passed as parameters in the decorator. For example:

```python
@<appname>.<httpmethod>('<path>', ..., status_code=<number>)
def <functionname>():
	...
	return <response>
```

> __Note__: if fastapi responses are used, the status code can be specified in the response class like this:
> ```python
> return JSONResponse(status_code=<number>, content=<response>)
> ``

Also, it is possible to get the status code from the `status` module of `fastapi`.

### Authentication
#### Token
The token authentication is used to authenticate the user. 