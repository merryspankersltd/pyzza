VERSION = '0.9 Napoletana'
DESCRIPTION = '''just some utilities and handlers for gtfs
with basilico and mozzarella'''

def version():
    return VERSION

def help():
    return '''
    Usage
    
    import pyzza
    pr = pyzza.repo(r'/path/to/repo')
    pr.get_expiry()'''