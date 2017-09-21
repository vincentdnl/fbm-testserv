message:
	./venv/bin/python main.py

run:
	./venv/bin/gunicorn server:app -k aiohttp.worker.GunicornWebWorker -b localhost:5050 --reload

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

.PHONY: config
config:
	cp -n config/config.template.yml config.yml
