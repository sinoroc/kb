#


build_dir := build
source_dir := src
sphinx_build := sphinx-build
sphinx_options := -c . -n -W


.DEFAULT_GOAL := all


.PHONY: clean
clean:
	$(RM) --recursive $(build_dir)/*


.PHONY: html latex
html: pdf
html latex:
	$(sphinx_build) $(sphinx_options) -b $@ $(source_dir) $(build_dir)/$@


.PHONY: pdf
pdf: latex
	$(MAKE) -C $(build_dir)/$<


.PHONY: all
all: html pdf


# Disable default rules and suffixes
# (improve speed and avoid unexpected behaviour)
MAKEFLAGS := --no-builtin-rules
.SUFFIXES:


# EOF
