from __init__ import create_app

app = create_app()
from rest_controller import *


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=9000, debug=True)

