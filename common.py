import codecs
import os
import sys
import logging

logging.basicConfig(filename="run.log", level=logging.INFO)

def to_json(python_object):
    if isinstance(python_object, bytes):
        return {'__class__': 'bytes',
                '__value__': codecs.encode(python_object, 'base64').decode()}
    raise TypeError(repr(python_object) + ' is not JSON serializable')


def from_json(json_object):
    if '__class__' in json_object and json_object['__class__'] == 'bytes':
        return codecs.decode(json_object['__value__'].encode(), 'base64')
    return json_object



def colors(state):
	color = ''

	if (state == 'BLUE'):
		color = '\033[94m'

	if (state == 'GREEN'):
		color = '\033[92m'

	if (state == 'YELLOW'):
		color = '\033[93m'

	if (state == 'RED'):
		color = '\033[91m'

	if (state == 'ENDC'):
		color = '\033[0m'

	if (state == 'WHITE'):
		color = '\033[0m'

	return color

def supports_color():
    """
    from https://github.com/django/django/blob/master/django/core/management/color.py
    Return True if the running system's terminal supports color,
    and False otherwise.
    """

    plat = sys.platform
    supported_platform = plat != 'Pocket PC' and (plat != 'win32' or 'ANSICON' in os.environ)

    # isatty is not always implemented, #6223.
    is_a_tty = hasattr(sys.stdout, 'isatty') and sys.stdout.isatty()
    if not supported_platform or not is_a_tty:
        return False
    return True

def log(string, color):
	logging.info(string)

	if not supports_color():
		print(string)
	else:
		print('\033[1m' + colors(color) + string + colors("ENDC"))

def seperator(color):
	logging.info("-" * 70)
	
	if not supports_color():
		print("-" * 70)
	else:
		print('\033[1m' + colors(color) + ("-" * 70) + colors("ENDC"))