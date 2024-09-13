.PHONY: venv
venv:
	python3.12 -m venv .venv

.PHONY: install-piptools
install-piptools:
	srcenv pip install pip-tools

.PHONY: install
install:
	srcenv pip install -r requirements.txt

.PHONY: run
run:
	srcenv python src/main.py

.PHONY: shell
shell:
	srcenv ipython -i src/main.py

.PHONY: pip-compile
pip-compile:
	srcenv pip-compile --output-file=requirements.txt requirements.in

.PHONY: update
update: pip-compile install

.PHONY: types
types:
	srcenv mypy src

.PHONY: format
format:
	srcenv ruff format src

.PHONY: lint
lint: types
	srcenv ruff check src

.PHONY: lint-fix
lint-fix:
	srcenv ruff check --fix src
