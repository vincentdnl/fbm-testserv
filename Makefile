message:
	./venv/bin/python main.py

run:
	./venv/bin/gunicorn app:app -k aiohttp.worker.GunicornWebWorker -b localhost:8080 --reload

install: install-virtualenv

create_virtualenv:
	rm -rf venv
	virtualenv -p python3.6 venv

install-virtualenv: create_virtualenv
	./venv/bin/pip install -r requirements.txt

clean_logs:
	rm -rf logs
	mkdir logs

requirements:
	./venv/bin/pip freeze > requirements.txt

tests:
	./scripts/tests.sh

watchtests:
	./scripts/watchtests.sh
