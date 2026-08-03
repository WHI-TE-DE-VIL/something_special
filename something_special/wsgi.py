import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'something_special.settings')

application = get_wsgi_application()
app = application
