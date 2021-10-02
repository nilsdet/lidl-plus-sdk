# LidlPlus client

```python
import os

from lidl_plus import LidlPlus

ACCESS_TOKEN = os.environ["LIDL_ACCESS_TOKEN"]

lidl = LidlPlus(access_token=ACCESS_TOKEN)
```
# Current functionality
## Get coupons
```python
coupons = lidl.coupons()
```
## Get receipts
```python
receipts = list(lidl.receipts())
```
## Get stores
```python
stores = lidl.stores()
```
## Get store by key
```python
store = lidl.stores.get(key=<KEY>)
```

# Todos
- [ ] Login with email and password and retrieve refresh token
- [ ] Refresh access token with refresh token
- [ ] Get receipt details by id
