VENV = .venv
PY = $(VENV)/bin/python

run: install
	cd src && ../$(PY) manage.py migrate
	cd src && ../$(PY) manage.py runserver

install:
	test -d $(VENV) || python3 -m venv $(VENV)
	$(VENV)/bin/pip install -r requirements.txt

clean:
	rm -rf $(VENV)

.PHONY: run install clean
