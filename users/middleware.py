from django.contrib.auth import authenticate, login

class RememberMeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        password = request.session.get('password ')
        username = request.session.get('username')
        if password  and username:
            user = authenticate(request, username=username , password=password)
            if user is not None:
                login(request, user)

        response = self.get_response(request)
        return response