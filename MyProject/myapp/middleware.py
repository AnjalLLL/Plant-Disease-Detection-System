from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin
from .db import get_db

class AuthenticationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Retrieve the auth_token from cookies
        auth_token = request.COOKIES.get('auth_token')
        
        if auth_token:
            # Connect to MongoDB
            db = get_db()
            user = db.user.find_one({"auth_token": auth_token})
            
            if user:
                # Attach user data to the request object
                request.user = user
            else:
                # Invalid token, treat as unauthenticated
                request.user = None
        else:
            # No token, treat as unauthenticated
            request.user = None

    def process_response(self, request, response):
        # Always return the response
        return response
