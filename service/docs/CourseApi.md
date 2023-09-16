# swagger_client.CourseApi

All URIs are relative to *http://127.0.0.1:8000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**course_create**](CourseApi.md#course_create) | **POST** /course/ | 
[**course_delete**](CourseApi.md#course_delete) | **DELETE** /course/{id}/ | 
[**course_list**](CourseApi.md#course_list) | **GET** /course/ | 
[**course_partial_update**](CourseApi.md#course_partial_update) | **PATCH** /course/{id}/ | 
[**course_read**](CourseApi.md#course_read) | **GET** /course/{id}/ | 
[**course_update**](CourseApi.md#course_update) | **PUT** /course/{id}/ | 

# **course_create**
> Course course_create(body)



### Example
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
api_instance = swagger_client.CourseApi(swagger_client.ApiClient(configuration))
body = swagger_client.Course() # Course | 

try:
    api_response = api_instance.course_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CourseApi->course_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Course**](Course.md)|  | 

### Return type

[**Course**](Course.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **course_delete**
> course_delete(id)



### Example
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
api_instance = swagger_client.CourseApi(swagger_client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this course.

try:
    api_instance.course_delete(id)
except ApiException as e:
    print("Exception when calling CourseApi->course_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this course. | 

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **course_list**
> InlineResponse2007 course_list(page=page, page_size=page_size, client=client, course_name=course_name, total_consumed_lessons=total_consumed_lessons, remaining_lessons=remaining_lessons, total_lessons=total_lessons, class_length=class_length, class_fee=class_fee)



### Example
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
api_instance = swagger_client.CourseApi(swagger_client.ApiClient(configuration))
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)
client = 'client_example' # str | 客户 ID (optional)
course_name = 'course_name_example' # str | 课程名称 (optional)
total_consumed_lessons = 56 # int | 总消耗课时 (optional)
remaining_lessons = 56 # int | 剩余课时 (optional)
total_lessons = 56 # int | 总课时 (optional)
class_length = 56 # int | 课时时长 (optional)
class_fee = 56 # int | 课时费用 (optional)

try:
    api_response = api_instance.course_list(page=page, page_size=page_size, client=client, course_name=course_name, total_consumed_lessons=total_consumed_lessons, remaining_lessons=remaining_lessons, total_lessons=total_lessons, class_length=class_length, class_fee=class_fee)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CourseApi->course_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **client** | **str**| 客户 ID | [optional] 
 **course_name** | **str**| 课程名称 | [optional] 
 **total_consumed_lessons** | **int**| 总消耗课时 | [optional] 
 **remaining_lessons** | **int**| 剩余课时 | [optional] 
 **total_lessons** | **int**| 总课时 | [optional] 
 **class_length** | **int**| 课时时长 | [optional] 
 **class_fee** | **int**| 课时费用 | [optional] 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **course_partial_update**
> Course course_partial_update(body, id)



### Example
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
api_instance = swagger_client.CourseApi(swagger_client.ApiClient(configuration))
body = swagger_client.Course() # Course | 
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this course.

try:
    api_response = api_instance.course_partial_update(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CourseApi->course_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Course**](Course.md)|  | 
 **id** | [**str**](.md)| A UUID string identifying this course. | 

### Return type

[**Course**](Course.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **course_read**
> Course course_read(id)



### Example
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
api_instance = swagger_client.CourseApi(swagger_client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this course.

try:
    api_response = api_instance.course_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CourseApi->course_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this course. | 

### Return type

[**Course**](Course.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **course_update**
> Course course_update(body, id)



### Example
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
api_instance = swagger_client.CourseApi(swagger_client.ApiClient(configuration))
body = swagger_client.Course() # Course | 
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this course.

try:
    api_response = api_instance.course_update(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CourseApi->course_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Course**](Course.md)|  | 
 **id** | [**str**](.md)| A UUID string identifying this course. | 

### Return type

[**Course**](Course.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

