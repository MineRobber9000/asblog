blog: in index.md
	autosite --auto

.PHONY: in
in: $(wildcard posts/*.md)
	python add_meta.py

index.md: $(wildcard posts/*.md)
	python generate_index.py
