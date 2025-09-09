from icecream import ic

class UserLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ic("uf", request.__dict__)
        if request.user.is_authenticated and hasattr(request.user, 'profile'):
            user_language = request.user.profile.app_language.code
            translation.activate(user_language)
        
        response = self.get_response(request)
        return response