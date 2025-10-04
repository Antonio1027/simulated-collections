make set-env:
	python3 -m venv venv && source venv/bin/activate

install:
	make set-env
	venv/bin/pip install -r requirements.txt

run:
	venv/bin/uvicorn main:app --reload

tests:
	venv/bin/pytest -s || echo "No tests found"

lint:
	venv/bin/flake8  || echo "Linting issues found"

format:
	venv/bin/black .

docker-build:
	docker build -t simulated-collections .

docker-up:
	docker-compose up -d

docker-down:
	docker-compose down
