#


build_dir := build
source_dir := src
sphinx_build := sphinx-build
sphinx_options := -n -W


.DEFAULT_GOAL := all


.PHONY: clean
clean:
	$(RM) --recursive $(build_dir)/*


.PHONY: html
html:
	$(sphinx_build) $(sphinx_options) -b $@ $(source_dir) $(build_dir)/$@


.PHONY: nothing
nothing:
	true


.PHONY: all
all: html


# EOF
