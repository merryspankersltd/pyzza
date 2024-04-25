# pyzza

> just some utilities and handlers for gtfs<br>
> with basilico and mozzarella

## usage

```python

>>> import pyzza

>>> # get lifespan for all gtfs in a repo 

>>> pr = pyzza.repo(r'/path/to/gtfs/zips')

>>> pr.get_expiry()

{['Planet Express': ...]}
