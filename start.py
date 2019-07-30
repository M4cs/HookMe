from app import app

if __name__ == "__main__":
    print('REQUEST http://localhost:5000 IN BROWSER TO START WEBHOOK SERVER')
    app.run('127.0.0.1')