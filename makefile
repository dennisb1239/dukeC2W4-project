install: 
	sudo apt install python-pip
	pip install --upgrade pip && pip install -r requirements.txt
				

test:
		python -m pytest -vv --cov


lint: 
		pylint --disable=R,C,W1203,E1101 cli mlib
		#lint Dockerfile
		#docker run --rm -i hadolint/hadolint < Dockerfile



all: install lint
