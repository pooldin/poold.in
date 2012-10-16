# Magical make incantations...
.DEFAULT_GOAL := deps

.PHONY: build clean deps dist run upload upload-dev upload-nightly \
		upload-release


REV=$(shell git rev-parse --short HEAD)
TIMESTAMP=$(shell date +'%s')
RUN=foreman run
SETUP=$(RUN) python setup.py
MANAGE=$(RUN) python manage.py


build:
	@$(SETUP) build

clean:
	@find . -name "*.py[co]" -exec rm -rf {} \;
	@$(SETUP) clean
	@rm -rf dist build

deps:
	@$(SETUP) develop

dist: clean
	@$(SETUP) sdist

run:
	@$(RUN) python -m pooldin.run

run-test:
	@foreman start

upload: upload-dev

upload-dev: clean
	@$(SETUP) egg_info --tag-build='-dev.$(TIMESTAMP).$(REV)' sdist upload -r pooldin

upload-nightly: clean
	@$(SETUP) egg_info --tag-date --tag-build='-dev' sdist upload -r pooldin

upload-release: clean
	@$(SETUP) sdist upload -r pooldin
