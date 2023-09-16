# swagger-client
QQAPP API Description

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: v1
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: Basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.AbrsmCompositionApi(swagger_client.ApiClient(configuration))
body = swagger_client.Composition() # Composition | 

try:
    api_response = api_instance.abrsm_composition_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AbrsmCompositionApi->abrsm_composition_create: %s\n" % e)
# Configure HTTP basic authorization: Basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.AbrsmCompositionApi(swagger_client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this composition.

try:
    api_instance.abrsm_composition_delete(id)
except ApiException as e:
    print("Exception when calling AbrsmCompositionApi->abrsm_composition_delete: %s\n" % e)
# Configure HTTP basic authorization: Basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.AbrsmCompositionApi(swagger_client.ApiClient(configuration))
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)

try:
    api_response = api_instance.abrsm_composition_list(page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AbrsmCompositionApi->abrsm_composition_list: %s\n" % e)
# Configure HTTP basic authorization: Basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.AbrsmCompositionApi(swagger_client.ApiClient(configuration))
body = swagger_client.Composition() # Composition | 
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this composition.

try:
    api_response = api_instance.abrsm_composition_partial_update(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AbrsmCompositionApi->abrsm_composition_partial_update: %s\n" % e)
# Configure HTTP basic authorization: Basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.AbrsmCompositionApi(swagger_client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this composition.

try:
    api_response = api_instance.abrsm_composition_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AbrsmCompositionApi->abrsm_composition_read: %s\n" % e)
# Configure HTTP basic authorization: Basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.AbrsmCompositionApi(swagger_client.ApiClient(configuration))
body = swagger_client.Composition() # Composition | 
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this composition.

try:
    api_response = api_instance.abrsm_composition_update(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AbrsmCompositionApi->abrsm_composition_update: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *http://127.0.0.1:8000/api*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AbrsmCompositionApi* | [**abrsm_composition_create**](docs/AbrsmCompositionApi.md#abrsm_composition_create) | **POST** /abrsm-composition/ | 
*AbrsmCompositionApi* | [**abrsm_composition_delete**](docs/AbrsmCompositionApi.md#abrsm_composition_delete) | **DELETE** /abrsm-composition/{id}/ | 
*AbrsmCompositionApi* | [**abrsm_composition_list**](docs/AbrsmCompositionApi.md#abrsm_composition_list) | **GET** /abrsm-composition/ | 
*AbrsmCompositionApi* | [**abrsm_composition_partial_update**](docs/AbrsmCompositionApi.md#abrsm_composition_partial_update) | **PATCH** /abrsm-composition/{id}/ | 
*AbrsmCompositionApi* | [**abrsm_composition_read**](docs/AbrsmCompositionApi.md#abrsm_composition_read) | **GET** /abrsm-composition/{id}/ | 
*AbrsmCompositionApi* | [**abrsm_composition_update**](docs/AbrsmCompositionApi.md#abrsm_composition_update) | **PUT** /abrsm-composition/{id}/ | 
*AbrsmExamApi* | [**abrsm_exam_create**](docs/AbrsmExamApi.md#abrsm_exam_create) | **POST** /abrsm-exam/ | 
*AbrsmExamApi* | [**abrsm_exam_delete**](docs/AbrsmExamApi.md#abrsm_exam_delete) | **DELETE** /abrsm-exam/{id}/ | 
*AbrsmExamApi* | [**abrsm_exam_list**](docs/AbrsmExamApi.md#abrsm_exam_list) | **GET** /abrsm-exam/ | 
*AbrsmExamApi* | [**abrsm_exam_partial_update**](docs/AbrsmExamApi.md#abrsm_exam_partial_update) | **PATCH** /abrsm-exam/{id}/ | 
*AbrsmExamApi* | [**abrsm_exam_read**](docs/AbrsmExamApi.md#abrsm_exam_read) | **GET** /abrsm-exam/{id}/ | 
*AbrsmExamApi* | [**abrsm_exam_update**](docs/AbrsmExamApi.md#abrsm_exam_update) | **PUT** /abrsm-exam/{id}/ | 
*AbrsmOrderApi* | [**abrsm_order_create**](docs/AbrsmOrderApi.md#abrsm_order_create) | **POST** /abrsm-order/ | 
*AbrsmOrderApi* | [**abrsm_order_delete**](docs/AbrsmOrderApi.md#abrsm_order_delete) | **DELETE** /abrsm-order/{id}/ | 
*AbrsmOrderApi* | [**abrsm_order_list**](docs/AbrsmOrderApi.md#abrsm_order_list) | **GET** /abrsm-order/ | 
*AbrsmOrderApi* | [**abrsm_order_partial_update**](docs/AbrsmOrderApi.md#abrsm_order_partial_update) | **PATCH** /abrsm-order/{id}/ | 
*AbrsmOrderApi* | [**abrsm_order_read**](docs/AbrsmOrderApi.md#abrsm_order_read) | **GET** /abrsm-order/{id}/ | 
*AbrsmOrderApi* | [**abrsm_order_update**](docs/AbrsmOrderApi.md#abrsm_order_update) | **PUT** /abrsm-order/{id}/ | 
*AbrsmPerformanceApi* | [**abrsm_performance_create**](docs/AbrsmPerformanceApi.md#abrsm_performance_create) | **POST** /abrsm-performance/ | 
*AbrsmPerformanceApi* | [**abrsm_performance_delete**](docs/AbrsmPerformanceApi.md#abrsm_performance_delete) | **DELETE** /abrsm-performance/{id}/ | 
*AbrsmPerformanceApi* | [**abrsm_performance_list**](docs/AbrsmPerformanceApi.md#abrsm_performance_list) | **GET** /abrsm-performance/ | 
*AbrsmPerformanceApi* | [**abrsm_performance_partial_update**](docs/AbrsmPerformanceApi.md#abrsm_performance_partial_update) | **PATCH** /abrsm-performance/{id}/ | 
*AbrsmPerformanceApi* | [**abrsm_performance_read**](docs/AbrsmPerformanceApi.md#abrsm_performance_read) | **GET** /abrsm-performance/{id}/ | 
*AbrsmPerformanceApi* | [**abrsm_performance_update**](docs/AbrsmPerformanceApi.md#abrsm_performance_update) | **PUT** /abrsm-performance/{id}/ | 
*AbrsmSuiteApi* | [**abrsm_suite_create**](docs/AbrsmSuiteApi.md#abrsm_suite_create) | **POST** /abrsm-suite/ | 
*AbrsmSuiteApi* | [**abrsm_suite_delete**](docs/AbrsmSuiteApi.md#abrsm_suite_delete) | **DELETE** /abrsm-suite/{id}/ | 
*AbrsmSuiteApi* | [**abrsm_suite_list**](docs/AbrsmSuiteApi.md#abrsm_suite_list) | **GET** /abrsm-suite/ | 
*AbrsmSuiteApi* | [**abrsm_suite_partial_update**](docs/AbrsmSuiteApi.md#abrsm_suite_partial_update) | **PATCH** /abrsm-suite/{id}/ | 
*AbrsmSuiteApi* | [**abrsm_suite_read**](docs/AbrsmSuiteApi.md#abrsm_suite_read) | **GET** /abrsm-suite/{id}/ | 
*AbrsmSuiteApi* | [**abrsm_suite_update**](docs/AbrsmSuiteApi.md#abrsm_suite_update) | **PUT** /abrsm-suite/{id}/ | 
*ClassSessionApi* | [**class_session_create**](docs/ClassSessionApi.md#class_session_create) | **POST** /class-session/ | 
*ClassSessionApi* | [**class_session_delete**](docs/ClassSessionApi.md#class_session_delete) | **DELETE** /class-session/{id}/ | 
*ClassSessionApi* | [**class_session_eliminate_session**](docs/ClassSessionApi.md#class_session_eliminate_session) | **GET** /class-session/{id}/eliminate_session/ | 
*ClassSessionApi* | [**class_session_list**](docs/ClassSessionApi.md#class_session_list) | **GET** /class-session/ | 
*ClassSessionApi* | [**class_session_partial_update**](docs/ClassSessionApi.md#class_session_partial_update) | **PATCH** /class-session/{id}/ | 
*ClassSessionApi* | [**class_session_read**](docs/ClassSessionApi.md#class_session_read) | **GET** /class-session/{id}/ | 
*ClassSessionApi* | [**class_session_update**](docs/ClassSessionApi.md#class_session_update) | **PUT** /class-session/{id}/ | 
*ClientApi* | [**client_create**](docs/ClientApi.md#client_create) | **POST** /client/ | 
*ClientApi* | [**client_delete**](docs/ClientApi.md#client_delete) | **DELETE** /client/{id}/ | 
*ClientApi* | [**client_list**](docs/ClientApi.md#client_list) | **GET** /client/ | 
*ClientApi* | [**client_partial_update**](docs/ClientApi.md#client_partial_update) | **PATCH** /client/{id}/ | 
*ClientApi* | [**client_read**](docs/ClientApi.md#client_read) | **GET** /client/{id}/ | 
*ClientApi* | [**client_update**](docs/ClientApi.md#client_update) | **PUT** /client/{id}/ | 
*CourseApi* | [**course_create**](docs/CourseApi.md#course_create) | **POST** /course/ | 
*CourseApi* | [**course_delete**](docs/CourseApi.md#course_delete) | **DELETE** /course/{id}/ | 
*CourseApi* | [**course_list**](docs/CourseApi.md#course_list) | **GET** /course/ | 
*CourseApi* | [**course_partial_update**](docs/CourseApi.md#course_partial_update) | **PATCH** /course/{id}/ | 
*CourseApi* | [**course_read**](docs/CourseApi.md#course_read) | **GET** /course/{id}/ | 
*CourseApi* | [**course_update**](docs/CourseApi.md#course_update) | **PUT** /course/{id}/ | 
*IncomeApi* | [**income_create**](docs/IncomeApi.md#income_create) | **POST** /income/ | 
*IncomeApi* | [**income_delete**](docs/IncomeApi.md#income_delete) | **DELETE** /income/{id}/ | 
*IncomeApi* | [**income_list**](docs/IncomeApi.md#income_list) | **GET** /income/ | 
*IncomeApi* | [**income_partial_update**](docs/IncomeApi.md#income_partial_update) | **PATCH** /income/{id}/ | 
*IncomeApi* | [**income_read**](docs/IncomeApi.md#income_read) | **GET** /income/{id}/ | 
*IncomeApi* | [**income_update**](docs/IncomeApi.md#income_update) | **PUT** /income/{id}/ | 
*LessonOpApi* | [**lesson_op_create**](docs/LessonOpApi.md#lesson_op_create) | **POST** /lesson-op/ | 
*LessonOpApi* | [**lesson_op_list**](docs/LessonOpApi.md#lesson_op_list) | **GET** /lesson-op/ | 
*LessonOpApi* | [**lesson_op_read**](docs/LessonOpApi.md#lesson_op_read) | **GET** /lesson-op/{id}/ | 
*VideoApi* | [**video_create**](docs/VideoApi.md#video_create) | **POST** /video/ | 
*VideoApi* | [**video_delete**](docs/VideoApi.md#video_delete) | **DELETE** /video/{id}/ | 
*VideoApi* | [**video_list**](docs/VideoApi.md#video_list) | **GET** /video/ | 
*VideoApi* | [**video_partial_update**](docs/VideoApi.md#video_partial_update) | **PATCH** /video/{id}/ | 
*VideoApi* | [**video_read**](docs/VideoApi.md#video_read) | **GET** /video/{id}/ | 
*VideoApi* | [**video_update**](docs/VideoApi.md#video_update) | **PUT** /video/{id}/ | 

## Documentation For Models

 - [ClassSession](docs/ClassSession.md)
 - [ClassSessionList](docs/ClassSessionList.md)
 - [Client](docs/Client.md)
 - [Composition](docs/Composition.md)
 - [Course](docs/Course.md)
 - [CourseList](docs/CourseList.md)
 - [Exam](docs/Exam.md)
 - [Income](docs/Income.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [InlineResponse20010](docs/InlineResponse20010.md)
 - [InlineResponse2002](docs/InlineResponse2002.md)
 - [InlineResponse2003](docs/InlineResponse2003.md)
 - [InlineResponse2004](docs/InlineResponse2004.md)
 - [InlineResponse2005](docs/InlineResponse2005.md)
 - [InlineResponse2006](docs/InlineResponse2006.md)
 - [InlineResponse2007](docs/InlineResponse2007.md)
 - [InlineResponse2008](docs/InlineResponse2008.md)
 - [InlineResponse2009](docs/InlineResponse2009.md)
 - [LessonOpLog](docs/LessonOpLog.md)
 - [LessonOpLogList](docs/LessonOpLogList.md)
 - [Order](docs/Order.md)
 - [Performance](docs/Performance.md)
 - [Suite](docs/Suite.md)
 - [Video](docs/Video.md)

## Documentation For Authorization


## Basic

- **Type**: HTTP basic authentication


## Author

