# Makefile for googlemaps Sphinx documentation

PYTHONPATH    = $(PYTHONPATH):../googlemaps
SPHINXBUILD   = sphinx-build

.PHONY: clean html

html:
	$(SPHINXBUILD) . html/

clean:
	-rm -rf html/
