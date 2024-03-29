NODE_MODULES ?= ./node_modules
JS_SENTINAL=$(NODE_MODULES)/sentinal
JSHINT=$(NODE_MODULES)/jshint/bin/jshint
JSCS=$(NODE_MODULES)/jscs/bin/jscs
REQUIREJS=$(NODE_MODULES)/.bin/r.js

jshint: $(JS_SENTINAL)
	$(JSHINT) $(JS_FILES)

jscs: $(JS_SENTINAL)
	$(JSCS) $(JS_FILES)

$(JS_SENTINAL): package.json
	rm -rf $(NODE_MODULES)
	npm install
	touch $(JS_SENTINAL)

static/js/main-built.js: $(JS_SENTINAL) build.js static/js/src static/js/libs
	$(REQUIREJS) -o build.js

js: static/js/main-built.js

.PHONY: js
