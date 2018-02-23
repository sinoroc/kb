..


********
Makefile
********

Links
=====

* https://www.gnu.org/software/make/manual/make.html

* http://clarkgrubb.com/makefile-style-guide


Example
=======

.. code-block:: makefile

    input_dir := input
    output_dir := output

    input_files := $(wildcard $(input_dir)/*.in)
    output_files := $(patsubst $(input_dir)/%.in,$(output_dir)/%.out,$(input_files))

    vpath %.in $(input_dir)

    .DEFAULT_GOAL := all

    .PHONY: all
    all: $(output_files)

    $(output_dir)/%.out: %.in | $(output_dir)
        cp $< $@

    $(output_dir):
        mkdir --parent $@

    .PHONY: clean
    clean:
        $(RM) $(output_files)

    # Disable default rules and suffixes
    # (improve speed and avoid unexpected behaviour)
    MAKEFLAGS := --no-builtin-rules
    .SUFFIXES:


.. EOF
