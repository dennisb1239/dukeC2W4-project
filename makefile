install: 
	sudo apt install python-pip
	pip install --upgrade pip && pip install -r requirements.txt
				

test:
		python -m pytest -vv --cov


lint: 
		pylint mlib cli
		#lint Dockerfile
		#docker run --rm -i hadolint/hadolint < Dockerfile



all: install lint test
