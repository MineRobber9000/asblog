PUBLISH_DIR:=/home/khuxkm/public_html/blog

blog: in index.md
	autosite --auto

.PHONY: in publish
in: $(wildcard posts/*.md)
	python add_meta.py

index.md: $(wildcard posts/*.md)
	python generate_index.py

publish: blog
	rm -rf $(PUBLISH_DIR)
	mv out $(PUBLISH_DIR)
