def wsgi_application(environ, start_response):
	status = '200 OK'
	respons_headers = [('Content-type','text/plain')]
	start_response(status, headers)
	resp = environ['QUERY_STRING'].split("&")
	resp = [item+"\r\n" for item in resp]
	return resp
