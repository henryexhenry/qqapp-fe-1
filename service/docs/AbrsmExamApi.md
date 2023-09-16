# swagger_client.AbrsmExamApi

All URIs are relative to *http://127.0.0.1:8000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**abrsm_exam_create**](AbrsmExamApi.md#abrsm_exam_create) | **POST** /abrsm-exam/ | 
[**abrsm_exam_delete**](AbrsmExamApi.md#abrsm_exam_delete) | **DELETE** /abrsm-exam/{id}/ | 
[**abrsm_exam_list**](AbrsmExamApi.md#abrsm_exam_list) | **GET** /abrsm-exam/ | 
[**abrsm_exam_partial_update**](AbrsmExamApi.md#abrsm_exam_partial_update) | **PATCH** /abrsm-exam/{id}/ | 
[**abrsm_exam_read**](AbrsmExamApi.md#abrsm_exam_read) | **GET** /abrsm-exam/{id}/ | 
[**abrsm_exam_update**](AbrsmExamApi.md#abrsm_exam_update) | **PUT** /abrsm-exam/{id}/ | 

# **abrsm_exam_create**
> Exam abrsm_exam_create(body)



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
api_instance = swagger_client.AbrsmExamApi(swagger_client.ApiClient(configuration))
body = swagger_client.Exam() # Exam | 

try:
    api_response = api_instance.abrsm_exam_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AbrsmExamApi->abrsm_exam_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Exam**](Exam.md)|  | 

### Return type

[**Exam**](Exam.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **abrsm_exam_delete**
> abrsm_exam_delete(id)



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
api_instance = swagger_client.AbrsmExamApi(swagger_client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this exam.

try:
    api_instance.abrsm_exam_delete(id)
except ApiException as e:
    print("Exception when calling AbrsmExamApi->abrsm_exam_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this exam. | 

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **abrsm_exam_list**
> InlineResponse2001 abrsm_exam_list(page=page, page_size=page_size)



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
api_instance = swagger_client.AbrsmExamApi(swagger_client.ApiClient(configuration))
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)

try:
    api_response = api_instance.abrsm_exam_list(page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AbrsmExamApi->abrsm_exam_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **abrsm_exam_partial_update**
> Exam abrsm_exam_partial_update(body, id)



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
api_instance = swagger_client.AbrsmExamApi(swagger_client.ApiClient(configuration))
body = swagger_client.Exam() # Exam | 
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this exam.

try:
    api_response = api_instance.abrsm_exam_partial_update(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AbrsmExamApi->abrsm_exam_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Exam**](Exam.md)|  | 
 **id** | [**str**](.md)| A UUID string identifying this exam. | 

### Return type

[**Exam**](Exam.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **abrsm_exam_read**
> Exam abrsm_exam_read(id)



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
api_instance = swagger_client.AbrsmExamApi(swagger_client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this exam.

try:
    api_response = api_instance.abrsm_exam_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AbrsmExamApi->abrsm_exam_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this exam. | 

### Return type

[**Exam**](Exam.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **abrsm_exam_update**
> Exam abrsm_exam_update(body, id)



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
api_instance = swagger_client.AbrsmExamApi(swagger_client.ApiClient(configuration))
body = swagger_client.Exam() # Exam | 
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this exam.

try:
    api_response = api_instance.abrsm_exam_update(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AbrsmExamApi->abrsm_exam_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Exam**](Exam.md)|  | 
 **id** | [**str**](.md)| A UUID string identifying this exam. | 

### Return type

[**Exam**](Exam.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

