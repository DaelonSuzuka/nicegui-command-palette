# **************************************************************************** #
# General Make configuration

# This suppresses make's command echoing. This suppression produces a cleaner output. 
# If you need to see the full commands being issued by make, comment this out.
MAKEFLAGS += -s

# Fix bad built-in make behaviors
MAKEFLAGS += --warn-undefined-variables
MAKEFLAGS += --no-builtin-rules

# **************************************************************************** #

# load the pypi credentials
ifneq (,$(wildcard .env))
include .env
# export them for twine
export
endif

# **************************************************************************** #
# Targets

build:
	uv build

publish:
	twine upload dist/* -u __token__

tests:
	$(VENV_PYTHON) -m pytest -s

coverage:
	$(VENV_PYTHON) -m pytest --cov

clean:
	rm -rf dist
