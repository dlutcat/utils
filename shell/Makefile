ORI_PTH = origin
ALL =  $(ORI_PTH)/jquery-1.5.1.min.js \
       $(ORI_PTH)/plugins/jquery.bgiframe.js \
       $(ORI_PTH)/plugins/jquery.cookie.js \
       $(ORI_PTH)/plugins/jquery-ui-1.8/jquery.ui.core.js \
       $(ORI_PTH)/plugins/jquery-ui-1.8/jquery.ui.widget.js \
       $(ORI_PTH)/plugins/jquery-ui-1.8/jquery.ui.position.js \
       $(ORI_PTH)/plugins/jquery-ui-1.8/jquery.ui.autocomplete.js \
       $(ORI_PTH)/plugins/jquery-ui-1.8/jquery.ui.dialog.js \
       $(ORI_PTH)/plugins/jquery.easing.1.3.js \
       $(ORI_PTH)/plugins/jquery.validationEngine.js \
       $(ORI_PTH)/plugins/jquery.placeholder.js \
       $(ORI_PTH)/plugins/jquery.fancybox-1.3.4.js \
       $(ORI_PTH)/plugins/jquery.fuwo.js \
       $(ORI_PTH)/global.js

MINI_ALL = $(ORI_PTH)/jquery-1.5.1.min.js \
           $(ORI_PTH)/plugins/jquery.cookie.js \
       	   $(ORI_PTH)/plugins/jquery.placeholder.js \
           $(ORI_PTH)/plugins/jquery.fancybox-1.3.4.js \
           $(ORI_PTH)/plugins/jquery.fuwo.js \
           $(ORI_PTH)/mini_global.js

REMOTE_SERVER = root@dev
REMOTE_JS_PTH = ~/hg_fuwo/fuwo_web/static/js/
#STAMP := $(shell date '+%y%m%d%k%M')
STAMP = 0726

all.js: 
	scp -r $(REMOTE_SERVER):$(REMOTE_JS_PTH)$(ORI_PTH)/ .; \
        cat $(ALL) > $(ORI_PTH)/all.js; \
        cat $(MINI_ALL) > $(ORI_PTH)/mini_all.js; \
        cp -r $(ORI_PTH) r$(STAMP); ./minify.sh r$(STAMP)

.PHONY: fetch compress update clean
fetch:
	scp -r $(REMOTE_SERVER):$(REMOTE_JS_PTH)$(ORI_PTH)/ .; \
        cat $(ALL) > $(ORI_PTH)/all.js; \
        cat $(MINI_ALL) > $(ORI_PTH)/mini_all.js

compress:
	cp -r $(ORI_PTH) r$(STAMP); ./minify.sh r$(STAMP)
update:
	scp -r r* $(REMOTE_SERVER):$(REMOTE_JS_PTH)
clean:
	-rm -rf r* $(ORI_PTH)
