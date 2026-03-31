import os
from waitress import serve

from workflow_project.wsgi import application

if __name__ == '__main__':
    port = int(os.environ.get('HTTP_PLATFORM_PORT', 8000))
    serve(application, host='127.0.0.1', port=port)