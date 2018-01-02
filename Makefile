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
html latex:
	$(sphinx_build) $(sphinx_options) -b $@ $(source_dir) $(build_dir)/$@


.PHONY: pdf
pdf: latex
	$(MAKE) -C $(build_dir)/$<


.PHONY: nothing
nothing:
	true


.PHONY: all
all: html latex pdf


# EOF
