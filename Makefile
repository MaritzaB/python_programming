clean:
	rm --recursive --force tests/__pychache__
	rm --recursive --force .pytest_cache

format:
	black --line-length 100 src/*.py
