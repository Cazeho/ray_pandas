import binascii
import re

IDENTIFIER_LENGTH = 20

# This prefix must match the value defined in ray_redis_module.cc.

def hex_identifier(identifier):
    return binascii.hexlify(identifier).decode()


def identifier(hex_identifier):
    return binascii.unhexlify(hex_identifier)

def key_to_hex_identifiers(key):
    # Extract worker_id and task_id from key of the form
    # prefix:worker_id:task_id.
    offset = key.index(b":") + 1
    worker_id = hex_identifier(key[offset:(offset + IDENTIFIER_LENGTH)])
    offset += IDENTIFIER_LENGTH + 1
    task_id = hex_identifier(key[offset:(offset + IDENTIFIER_LENGTH)])
    return worker_id, task_id

def clean(sometext):
    sometext = sometext.decode('UTF-8')
    ansi_escape = re.compile(r'\x1b[^m]*m')
    return ansi_escape.sub('', sometext)