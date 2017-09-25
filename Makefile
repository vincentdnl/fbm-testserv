PORT = 5050


run:
	./venv/bin/gunicorn server:app -k aiohttp.worker.GunicornWebWorker -b localhost:${PORT} --reload

message:
	./venv/bin/python main.py

################
## Virtualenv ##
################
install: install-virtualenv

create_virtualenv:
	rm -rf venv
	virtualenv -p python3.6 venv

install-virtualenv: create_virtualenv
	./venv/bin/pip install -r requirements.txt
