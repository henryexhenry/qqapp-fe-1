# swagger_client.ClassSessionApi

All URIs are relative to *http://127.0.0.1:8000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**class_session_create**](ClassSessionApi.md#class_session_create) | **POST** /class-session/ | 
[**class_session_delete**](ClassSessionApi.md#class_session_delete) | **DELETE** /class-session/{id}/ | 
[**class_session_eliminate_session**](ClassSessionApi.md#class_session_eliminate_session) | **GET** /class-session/{id}/eliminate_session/ | 
[**class_session_list**](ClassSessionApi.md#class_session_list) | **GET** /class-session/ | 
[**class_session_partial_update**](ClassSessionApi.md#class_session_partial_update) | **PATCH** /class-session/{id}/ | 
[**class_session_read**](ClassSessionApi.md#class_session_read) | **GET** /class-session/{id}/ | 
[**class_session_update**](ClassSessionApi.md#class_session_update) | **PUT** /class-session/{id}/ | 

# **class_session_create**
> ClassSession class_session_create(body)



check if time period overlaps

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
api_instance = swagger_client.ClassSessionApi(swagger_client.ApiClient(configuration))
body = swagger_client.ClassSession() # ClassSession | 

try:
    api_response = api_instance.class_session_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClassSessionApi->class_session_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClassSession**](ClassSession.md)|  | 

### Return type

[**ClassSession**](ClassSession.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **class_session_delete**
> class_session_delete(id)



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
api_instance = swagger_client.ClassSessionApi(swagger_client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this class session.

try:
    api_instance.class_session_delete(id)
except ApiException as e:
    print("Exception when calling ClassSessionApi->class_session_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this class session. | 

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **class_session_eliminate_session**
> ClassSession class_session_eliminate_session(id)



Eliminate a class session

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
api_instance = swagger_client.ClassSessionApi(swagger_client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this class session.

try:
    api_response = api_instance.class_session_eliminate_session(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClassSessionApi->class_session_eliminate_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this class session. | 

### Return type

[**ClassSession**](ClassSession.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **class_session_list**
> InlineResponse2005 class_session_list(page=page, page_size=page_size, status=status, course=course, start_time=start_time, end_time=end_time)



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
api_instance = swagger_client.ClassSessionApi(swagger_client.ApiClient(configuration))
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)
status = 56 # int | 0: 结课, 1: 待上课, 2: 待排课 (optional)
course = 'course_example' # str | 课程id (optional)
start_time = 'start_time_example' # str | 开始时间 (optional)
end_time = 'end_time_example' # str | 结束时间 (optional)

try:
    api_response = api_instance.class_session_list(page=page, page_size=page_size, status=status, course=course, start_time=start_time, end_time=end_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClassSessionApi->class_session_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **status** | **int**| 0: 结课, 1: 待上课, 2: 待排课 | [optional] 
 **course** | **str**| 课程id | [optional] 
 **start_time** | **str**| 开始时间 | [optional] 
 **end_time** | **str**| 结束时间 | [optional] 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **class_session_partial_update**
> ClassSession class_session_partial_update(body, id)



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
api_instance = swagger_client.ClassSessionApi(swagger_client.ApiClient(configuration))
body = swagger_client.ClassSession() # ClassSession | 
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this class session.

try:
    api_response = api_instance.class_session_partial_update(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClassSessionApi->class_session_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClassSession**](ClassSession.md)|  | 
 **id** | [**str**](.md)| A UUID string identifying this class session. | 

### Return type

[**ClassSession**](ClassSession.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **class_session_read**
> ClassSessionList class_session_read(id)



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
api_instance = swagger_client.ClassSessionApi(swagger_client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this class session.

try:
    api_response = api_instance.class_session_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClassSessionApi->class_session_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this class session. | 

### Return type

[**ClassSessionList**](ClassSessionList.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **class_session_update**
> ClassSession class_session_update(body, id)



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
api_instance = swagger_client.ClassSessionApi(swagger_client.ApiClient(configuration))
body = swagger_client.ClassSession() # ClassSession | 
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this class session.

try:
    api_response = api_instance.class_session_update(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClassSessionApi->class_session_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClassSession**](ClassSession.md)|  | 
 **id** | [**str**](.md)| A UUID string identifying this class session. | 

### Return type

[**ClassSession**](ClassSession.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

