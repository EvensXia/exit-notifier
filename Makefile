PYTHON_PATH=`which python`

format: ## apply autopep8 and import sort
	$(PYTHON_PATH) -m autopep8 .
	$(PYTHON_PATH) -m isort .

reinstall:
	$(PYTHON_PATH) -m pip uninstall exit-notifier -y
	$(PYTHON_PATH) -m poetry build
	$(PYTHON_PATH) -m pip install dist/*.whl

rm:
	$(PYTHON_PATH) -m pip uninstall exit-notifier -y


