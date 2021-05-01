# def open_access_middleware(get_response):
#     def middleware(request):
#         response = get_response(request)
#         response["Access-Control-Allow-Origin"] = "http://localhost:3000"
#         response["Access-Control-Allow-Methods"] = "GET,HEAD,OPTIONS,POST,PUT"
#         response["Access-Control-Allow-Headers"] = "Origin, X-Requested-With, Content-Type, Accept, Authorization, x-csrftoken"
#         return response
#     return middleware
