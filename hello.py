def wsgi_application(environ, start_response):
	status = '200 OK'
	headers = [
		('Content-Type', 'text/plan')
	]
	body = "Hello, world!"
	start_response(status, headers)
	return [ body ]
"\n".join(environ.get('QUERY_STRING').split("&"))
