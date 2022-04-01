
.PHONY: \
	clean \
	format \
	tests

clean:
	rm --recursive --force */__pycache__
	rm --recursive --force .pytest_cache
	rm --recursive --force __pycache__

format:
	black --line-length 100 src/*.py

tests:
	pytest --verbose tests/