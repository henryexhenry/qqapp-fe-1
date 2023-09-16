# swagger_client.LessonOpApi

All URIs are relative to *http://127.0.0.1:8000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**lesson_op_create**](LessonOpApi.md#lesson_op_create) | **POST** /lesson-op/ | 
[**lesson_op_list**](LessonOpApi.md#lesson_op_list) | **GET** /lesson-op/ | 
[**lesson_op_read**](LessonOpApi.md#lesson_op_read) | **GET** /lesson-op/{id}/ | 

# **lesson_op_create**
> LessonOpLog lesson_op_create(body)



- 续课时 - 消课时

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
api_instance = swagger_client.LessonOpApi(swagger_client.ApiClient(configuration))
body = swagger_client.LessonOpLog() # LessonOpLog | 

try:
    api_response = api_instance.lesson_op_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LessonOpApi->lesson_op_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LessonOpLog**](LessonOpLog.md)|  | 

### Return type

[**LessonOpLog**](LessonOpLog.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lesson_op_list**
> InlineResponse2009 lesson_op_list(page=page, page_size=page_size, course=course, op_type=op_type)



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
api_instance = swagger_client.LessonOpApi(swagger_client.ApiClient(configuration))
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)
course = 'course_example' # str | 課程 ID (optional)
op_type = 56 # int | 操作: 0-消課, 1-續課 (optional)

try:
    api_response = api_instance.lesson_op_list(page=page, page_size=page_size, course=course, op_type=op_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LessonOpApi->lesson_op_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **course** | **str**| 課程 ID | [optional] 
 **op_type** | **int**| 操作: 0-消課, 1-續課 | [optional] 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lesson_op_read**
> LessonOpLogList lesson_op_read(id)



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
api_instance = swagger_client.LessonOpApi(swagger_client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this lesson op log.

try:
    api_response = api_instance.lesson_op_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LessonOpApi->lesson_op_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this lesson op log. | 

### Return type

[**LessonOpLogList**](LessonOpLogList.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

