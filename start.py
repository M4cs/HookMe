from app import app
from crayons import *


if __name__ == "__main__":
    print(green('RUN: "ngrok http 5000", IN ANOTHER TERMINAL WINDOW TO PORT FORWARD'))
    app.run('0.0.0.0', port=5050)
