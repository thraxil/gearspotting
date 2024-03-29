# default config values that can all be overridden
VE ?= ./ve
MANAGE ?= ./manage.py
FLAKE8 ?= $(VE)/bin/flake8
SYS_PYTHON ?= python3
PIP ?= $(VE)/bin/pip3
SENTINAL ?= $(VE)/sentinal
REQUIREMENTS ?= requirements.txt
TAG ?= latest
IMAGE ?= $(REPO)/$(APP):$(TAG)

JS_FILES ?= static/js/

ifeq ($(TAG), undefined)
	IMAGE ?= $(REPO)/$(APP)
else
	IMAGE ?= $(REPO)/$(APP):$(TAG)
endif

MAX_COMPLEXITY ?= 10

