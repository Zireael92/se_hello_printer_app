.PHONY: test

deps:
	pip install -r requirements.txt; \
  pip install -r test_requirements.txt

test:
	PYTHONPATH=. py.test --verbose -s

lint:
	flake8 hello_world test

run:
	python3 main.py

test_smoke:
	curl --fail 127.0.0.1:5000

test_cov:
	PYTHONPATH=. py.test --verbose -s --cov=.

test_xunit:
	PYTHONPATH=. py.test --verbose -s --cov-report xml --junit-xml=test_results.xml


docker_build:
	docker build -t hello_world_printer .

docker_run: docker_build
	docker run \
	 --name hello_world_printer_dev \
	  -p 5000:5000 \
		-d hello_world_printer

USERNAME=Zireael92
TAG=$(USERNAME)/hello_world_printer

docker_push: docker_build
	@docker login --username $(USERNAME) --password $${DOCKER_PASSWORD}; \
	docker tag hello-world-printer $(TAG); \
	docker push $(TAG); \
	docker logout;
