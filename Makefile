REPO=thraxil
APP=gearspotting

ifeq ($(TAG), undefined)
	IMAGE = localhost:5000/thraxil/$(APP)
else
	IMAGE = localhost:5000/thraxil/$(APP):$(TAG)
endif

include *.mk
