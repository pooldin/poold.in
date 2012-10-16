import os
from pooldin import app


def main():
    port = int(os.environ.get('PORT', 5000))
    host = os.environ.get('HOST', '0.0.0.0')
    app.run(port=port, host=host, debug=True)

if __name__ == '__main__':
    main()
