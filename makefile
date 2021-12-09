install: 
	apt install python3-pip
	pip install pip && pip install -r requirements.txt
				

test:
		python -m pytest -vv 



format: 
		black *.py 


lint: 
		pylint --disable=R,C
		#lint Dockerfile
		#docker run --rm -i hadolint/hadolint < Dockerfile



all: install lint test
