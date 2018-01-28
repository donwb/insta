#
# The include should be a single file that contains:
# export USER := {user}
# export PASSWORD := {password}
#
include env

$(info $$USER is [${INSTA_USER}])
$(info $$PASSWORD is [${INSTA_PASSWORD}])
$(info $$TEST_USER_ID is [${TEST_USER_ID}])
$(info $$RUN_USER_ID is [${RUN_USER_ID}])

all:
	python3 main.py

.PHONY: all 