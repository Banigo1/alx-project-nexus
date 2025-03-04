from django.utils.deprecation import MiddlewareMixin
from django.core.cache import cache
import time

class PollMetricsMiddleware(MiddlewareMixin):
    """
    Middleware to track and optimize poll performance metrics.
    """
    def process_request(self, request):
        request.start_time = time.time()
    
    def process_response(self, request, response):
        if not hasattr(request, 'start_time'):
            return response
        
        # Calculate request duration
        duration = time.time() - request.start_time
        
        # Only log metrics for poll-related endpoints
        if '/api/polls/' in request.path:
            path_key = request.path.replace('/', '_')
            # Update average response time in cache
            avg_time = cache.get(f'avg_time{path_key}', 0)
            count = cache.get(f'count{path_key}', 0)
            
            if count > 0:
                avg_time = (avg_time * count + duration) / (count + 1)
            else:
                avg_time = duration
                
            cache.set(f'avg_time{path_key}', avg_time, 3600)
            cache.set(f'count{path_key}', count + 1, 3600)
            
            # Add helpful headers for developers in development
            response['X-Poll-API-Time'] = str(round(duration * 1000, 2)) + 'ms'
        
        return response