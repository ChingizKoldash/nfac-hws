def application(environ, start_response):
    path = environ.get('PATH_INFO', '')
    method = environ.get('REQUEST_METHOD', '')
    
    if path == '/ping' and method == 'GET':
        start_response('200 OK', [('Content-Type', 'text/plain')])
        return [b'pong']
    
    elif path == '/info' and method == 'GET':
        response_body = f"Method: {method}\nURL: {environ.get('RAW_URI', '')}\nProtocol: {environ.get('SERVER_PROTOCOL', '')}"
        start_response('200 OK', [('Content-Type', 'text/plain')])
        return [response_body.encode('utf-8')]
    
    else:
        start_response('404 Not Found', [('Content-Type', 'text/plain')])
        return [b'Not Found']