#
# The include should be a single file that contains:
# export USER := {user}
# export PASSWORD := {password}
#
include env

$(info $$USER is [${INSTA_USER}])
$(info $$PASSWORD is [${INSTA_PASSWORD}])

all:
	python3 main.py

.PHONY: all 