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
	python3 cli.py broadcast ${TEST_USER_ID}

test:
	python3 cli.py user ${TEST_USER}

find:
	python3 cli.py user ${USER}

user:
	python3 cli.py broadcast ${USERID}

.PHONY: all test find user