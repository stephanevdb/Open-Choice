from waitress import serve
from app import app

if __name__ == '__main__':
    print("Starting server")
    print("Server running on port 8737")
    serve(app, host='0.0.0.0', port=8737)
    print("Server stopped")

    