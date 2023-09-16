# swagger_client.AbrsmSuiteApi

All URIs are relative to *http://127.0.0.1:8000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**abrsm_suite_create**](AbrsmSuiteApi.md#abrsm_suite_create) | **POST** /abrsm-suite/ | 
[**abrsm_suite_delete**](AbrsmSuiteApi.md#abrsm_suite_delete) | **DELETE** /abrsm-suite/{id}/ | 
[**abrsm_suite_list**](AbrsmSuiteApi.md#abrsm_suite_list) | **GET** /abrsm-suite/ | 
[**abrsm_suite_partial_update**](AbrsmSuiteApi.md#abrsm_suite_partial_update) | **PATCH** /abrsm-suite/{id}/ | 
[**abrsm_suite_read**](AbrsmSuiteApi.md#abrsm_suite_read) | **GET** /abrsm-suite/{id}/ | 
[**abrsm_suite_update**](AbrsmSuiteApi.md#abrsm_suite_update) | **PUT** /abrsm-suite/{id}/ | 

# **abrsm_suite_create**
> Suite abrsm_suite_create(body)



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
api_instance = swagger_client.AbrsmSuiteApi(swagger_client.ApiClient(configuration))
body = swagger_client.Suite() # Suite | 

try:
    api_response = api_instance.abrsm_suite_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AbrsmSuiteApi->abrsm_suite_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Suite**](Suite.md)|  | 

### Return type

[**Suite**](Suite.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **abrsm_suite_delete**
> abrsm_suite_delete(id)



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
api_instance = swagger_client.AbrsmSuiteApi(swagger_client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this suite.

try:
    api_instance.abrsm_suite_delete(id)
except ApiException as e:
    print("Exception when calling AbrsmSuiteApi->abrsm_suite_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this suite. | 

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **abrsm_suite_list**
> InlineResponse2004 abrsm_suite_list(page=page, page_size=page_size)



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
api_instance = swagger_client.AbrsmSuiteApi(swagger_client.ApiClient(configuration))
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)

try:
    api_response = api_instance.abrsm_suite_list(page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AbrsmSuiteApi->abrsm_suite_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **abrsm_suite_partial_update**
> Suite abrsm_suite_partial_update(body, id)



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
api_instance = swagger_client.AbrsmSuiteApi(swagger_client.ApiClient(configuration))
body = swagger_client.Suite() # Suite | 
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this suite.

try:
    api_response = api_instance.abrsm_suite_partial_update(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AbrsmSuiteApi->abrsm_suite_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Suite**](Suite.md)|  | 
 **id** | [**str**](.md)| A UUID string identifying this suite. | 

### Return type

[**Suite**](Suite.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **abrsm_suite_read**
> Suite abrsm_suite_read(id)



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
api_instance = swagger_client.AbrsmSuiteApi(swagger_client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this suite.

try:
    api_response = api_instance.abrsm_suite_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AbrsmSuiteApi->abrsm_suite_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this suite. | 

### Return type

[**Suite**](Suite.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **abrsm_suite_update**
> Suite abrsm_suite_update(body, id)



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
api_instance = swagger_client.AbrsmSuiteApi(swagger_client.ApiClient(configuration))
body = swagger_client.Suite() # Suite | 
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this suite.

try:
    api_response = api_instance.abrsm_suite_update(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AbrsmSuiteApi->abrsm_suite_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Suite**](Suite.md)|  | 
 **id** | [**str**](.md)| A UUID string identifying this suite. | 

### Return type

[**Suite**](Suite.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

