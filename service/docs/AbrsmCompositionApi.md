# swagger_client.AbrsmCompositionApi

All URIs are relative to *http://127.0.0.1:8000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**abrsm_composition_create**](AbrsmCompositionApi.md#abrsm_composition_create) | **POST** /abrsm-composition/ | 
[**abrsm_composition_delete**](AbrsmCompositionApi.md#abrsm_composition_delete) | **DELETE** /abrsm-composition/{id}/ | 
[**abrsm_composition_list**](AbrsmCompositionApi.md#abrsm_composition_list) | **GET** /abrsm-composition/ | 
[**abrsm_composition_partial_update**](AbrsmCompositionApi.md#abrsm_composition_partial_update) | **PATCH** /abrsm-composition/{id}/ | 
[**abrsm_composition_read**](AbrsmCompositionApi.md#abrsm_composition_read) | **GET** /abrsm-composition/{id}/ | 
[**abrsm_composition_update**](AbrsmCompositionApi.md#abrsm_composition_update) | **PUT** /abrsm-composition/{id}/ | 

# **abrsm_composition_create**
> Composition abrsm_composition_create(body)



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
api_instance = swagger_client.AbrsmCompositionApi(swagger_client.ApiClient(configuration))
body = swagger_client.Composition() # Composition | 

try:
    api_response = api_instance.abrsm_composition_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AbrsmCompositionApi->abrsm_composition_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Composition**](Composition.md)|  | 

### Return type

[**Composition**](Composition.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **abrsm_composition_delete**
> abrsm_composition_delete(id)



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
api_instance = swagger_client.AbrsmCompositionApi(swagger_client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this composition.

try:
    api_instance.abrsm_composition_delete(id)
except ApiException as e:
    print("Exception when calling AbrsmCompositionApi->abrsm_composition_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this composition. | 

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **abrsm_composition_list**
> InlineResponse200 abrsm_composition_list(page=page, page_size=page_size)



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
api_instance = swagger_client.AbrsmCompositionApi(swagger_client.ApiClient(configuration))
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)

try:
    api_response = api_instance.abrsm_composition_list(page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AbrsmCompositionApi->abrsm_composition_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **abrsm_composition_partial_update**
> Composition abrsm_composition_partial_update(body, id)



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
api_instance = swagger_client.AbrsmCompositionApi(swagger_client.ApiClient(configuration))
body = swagger_client.Composition() # Composition | 
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this composition.

try:
    api_response = api_instance.abrsm_composition_partial_update(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AbrsmCompositionApi->abrsm_composition_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Composition**](Composition.md)|  | 
 **id** | [**str**](.md)| A UUID string identifying this composition. | 

### Return type

[**Composition**](Composition.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **abrsm_composition_read**
> Composition abrsm_composition_read(id)



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
api_instance = swagger_client.AbrsmCompositionApi(swagger_client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this composition.

try:
    api_response = api_instance.abrsm_composition_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AbrsmCompositionApi->abrsm_composition_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this composition. | 

### Return type

[**Composition**](Composition.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **abrsm_composition_update**
> Composition abrsm_composition_update(body, id)



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
api_instance = swagger_client.AbrsmCompositionApi(swagger_client.ApiClient(configuration))
body = swagger_client.Composition() # Composition | 
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this composition.

try:
    api_response = api_instance.abrsm_composition_update(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AbrsmCompositionApi->abrsm_composition_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Composition**](Composition.md)|  | 
 **id** | [**str**](.md)| A UUID string identifying this composition. | 

### Return type

[**Composition**](Composition.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

