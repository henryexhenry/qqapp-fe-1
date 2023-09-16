# swagger_client.AbrsmOrderApi

All URIs are relative to *http://127.0.0.1:8000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**abrsm_order_create**](AbrsmOrderApi.md#abrsm_order_create) | **POST** /abrsm-order/ | 
[**abrsm_order_delete**](AbrsmOrderApi.md#abrsm_order_delete) | **DELETE** /abrsm-order/{id}/ | 
[**abrsm_order_list**](AbrsmOrderApi.md#abrsm_order_list) | **GET** /abrsm-order/ | 
[**abrsm_order_partial_update**](AbrsmOrderApi.md#abrsm_order_partial_update) | **PATCH** /abrsm-order/{id}/ | 
[**abrsm_order_read**](AbrsmOrderApi.md#abrsm_order_read) | **GET** /abrsm-order/{id}/ | 
[**abrsm_order_update**](AbrsmOrderApi.md#abrsm_order_update) | **PUT** /abrsm-order/{id}/ | 

# **abrsm_order_create**
> Order abrsm_order_create(body)



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
api_instance = swagger_client.AbrsmOrderApi(swagger_client.ApiClient(configuration))
body = swagger_client.Order() # Order | 

try:
    api_response = api_instance.abrsm_order_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AbrsmOrderApi->abrsm_order_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Order**](Order.md)|  | 

### Return type

[**Order**](Order.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **abrsm_order_delete**
> abrsm_order_delete(id)



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
api_instance = swagger_client.AbrsmOrderApi(swagger_client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this order.

try:
    api_instance.abrsm_order_delete(id)
except ApiException as e:
    print("Exception when calling AbrsmOrderApi->abrsm_order_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this order. | 

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **abrsm_order_list**
> InlineResponse2002 abrsm_order_list(page=page, page_size=page_size)



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
api_instance = swagger_client.AbrsmOrderApi(swagger_client.ApiClient(configuration))
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)

try:
    api_response = api_instance.abrsm_order_list(page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AbrsmOrderApi->abrsm_order_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **abrsm_order_partial_update**
> Order abrsm_order_partial_update(body, id)



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
api_instance = swagger_client.AbrsmOrderApi(swagger_client.ApiClient(configuration))
body = swagger_client.Order() # Order | 
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this order.

try:
    api_response = api_instance.abrsm_order_partial_update(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AbrsmOrderApi->abrsm_order_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Order**](Order.md)|  | 
 **id** | [**str**](.md)| A UUID string identifying this order. | 

### Return type

[**Order**](Order.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **abrsm_order_read**
> Order abrsm_order_read(id)



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
api_instance = swagger_client.AbrsmOrderApi(swagger_client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this order.

try:
    api_response = api_instance.abrsm_order_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AbrsmOrderApi->abrsm_order_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this order. | 

### Return type

[**Order**](Order.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **abrsm_order_update**
> Order abrsm_order_update(body, id)



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
api_instance = swagger_client.AbrsmOrderApi(swagger_client.ApiClient(configuration))
body = swagger_client.Order() # Order | 
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this order.

try:
    api_response = api_instance.abrsm_order_update(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AbrsmOrderApi->abrsm_order_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Order**](Order.md)|  | 
 **id** | [**str**](.md)| A UUID string identifying this order. | 

### Return type

[**Order**](Order.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

