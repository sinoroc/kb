#


build_dir := build
source_dir := src
sphinx_build := sphinx-build


.DEFAULT_GOAL := all


.PHONY: clean
clean:
	$(RM) --recursive $(build_dir)/*


.PHONY: html
html:
	$(sphinx_build) -b $@ $(source_dir) $(build_dir)/$@


.PHONY: nothing
nothing:
	true


.PHONY: all
all: html


# EOF
