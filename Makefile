all: black isort flake8 mypy pytest

black:
	black -v --exclude="(.pytest_cache\/*|.mypy_cache\/*)" .

isort:
	isort .

flake8:
	flake8 .

mypy:
	mypy .

pytest:
	pytest -v .

build:
	rm -rf dist/*
	rm -rf build/*
	python setup.py sdist
	python setup.py bdist_wheel

upload-test:
	twine upload --repository testpypi dist/*

upload:
	twine upload --repository pypi dist/*
