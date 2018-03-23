.PHONY: protoc test

protoc:
	protoc --python_out=src -Isrc src/tests/sample.proto

test:
	python setup.py nosetests
