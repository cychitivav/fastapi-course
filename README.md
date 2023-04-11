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
# FastAPI courses
The information in this directory is the result of the FastAPI courses given by [Platzi](https://platzi.com/cursos/fastapi/).

[**Explore the docs »**](https://github.com/cychitivav/fastapi_course/wiki)

[View Demo](https://github.com/cychitivav/fastapi_course) · [Report Bug](https://github.com/cychitivav/fastapi_course/issues) · [Request Feature](https://github.com/cychitivav/fastapi_course/issues)

[![Contributors](https://img.shields.io/github/contributors/cychitivav/fastapi_course.svg?style=for-the-badge)](https://github.com/cychitivav/fastapi_course/graphs/contributors)
[![Forks](https://img.shields.io/github/forks/cychitivav/fastapi_course.svg?style=for-the-badge)](https://github.com/cychitivav/fastapi_course/network/members)
[![Stargazers](https://img.shields.io/github/stars/cychitivav/fastapi_course.svg?style=for-the-badge)](https://github.com/cychitivav/fastapi_course/stargazers)
[![Issues](https://img.shields.io/github/issues/cychitivav/fastapi_course.svg?style=for-the-badge)](https://github.com/cychitivav/fastapi_course/issues)
[![MIT License](https://img.shields.io/github/license/cychitivav/fastapi_course.svg?style=for-the-badge)](https://github.com/cychitivav/fastapi_course/blob/main/LICENSE)


</div>


<!-- TABLE OF CONTENTS -->
<!-- omit in toc -->
## Table of contents
- [What is FastAPI?](#what-is-fastapi)
	- [Previous knowledge](#previous-knowledge)
- [Run the project](#run-the-project)
- [Run the project without Docker](#run-the-project-without-docker)
	- [Useful flags](#useful-flags)
- [Documentation with Swagger UI](#documentation-with-swagger-ui)
- [HTTP methods](#http-methods)
	- [Create a resource](#create-a-resource)
	- [Parameters](#parameters)
		- [Path](#path)
		- [Query](#query)



## What is FastAPI?
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


## Run the project
To run an application in this repository, just clone the repository and run the following command:

```bash
./docker/start.sh <filename>:<appname>
```

This script will create a docker container with the necessary dependencies to run the application using the `uvicorn` server. The application will be available in `http://localhost:5000`.

## Run the project without Docker
To run an application in this repository without Docker, just clone the repository and run the following command (make sure to have the dependencies installed):

```bash
uvicorn <filename>:<appname>
```

### Useful flags
| Flag | Description |
| --- | --- |
| `--reload` | Automatically reload the server when a change is made. |
| `--port` | Specify the port to run the server. |
| `--host` | Specify the host to run the server. |

> __Note__: In WSL2, it is necessary to specify the host as `0.0.0.0` to be able to access the server from the browser. This is because the app is running in a virtual machine and to access from another machine, it is necessary to specify the host.

## Documentation with Swagger UI
To access the documentation, it is just necessary add `/docs` to the URL. For example, if the server is running in `http://localhost:8000`, the documentation will be in `http://localhost:8000/docs`.

<div align="center">
	<img src="https://user-images.githubusercontent.com/30636259/231292366-aa6cf1a4-57c7-49e2-831c-69163ad8b3d5.png" alt="Logo" width="650"/>
</div>

## HTTP methods
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
This type of parameter is used to specify the resource that will be retrieved and it will call the server with the url `http://localhost:8000/<path>?<parameter1>=<value1>&<parameter2>=<value2>`.

```python
@<appname>.<httpmethod>('<path>')
def <functionname>(<parameter1>: <type>, <parameter2>: <type>):
	...
	return <response>
```

> **Note**: The only difference between the `Path` and `Query` parameters is that the `Path` parameter must be specified in the decorator and in the function, and the `Query` parameter must just be specified in the function.

