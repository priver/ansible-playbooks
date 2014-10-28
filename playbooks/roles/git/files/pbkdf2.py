#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""PBKDF2 password encode and verify functions.

Based on Django ones.
https://github.com/django/django
"""
import argparse
import base64
import binascii
import hashlib
import hmac
import json
import random
import struct


def store(username, password, iterations, filename):
    """Encode password and store it in file."""
    with open(filename, 'w+') as passwd_file:
        try:
            passwords = json.load(passwd_file)
        except ValueError:
            passwords = {}
        passwords[username] = encode(password, gen_salt(), iterations)
        json.dump(passwords, passwd_file, indent=4)
        passwd_file.write('\n')


def verify(username, password, filename):
    """Check if the given password is correct."""
    with open(filename, 'r') as passwd_file:
        try:
            passwords = json.load(passwd_file)
        except ValueError:
            passwords = {}
    try:
        iterations, salt, hash = passwords[username].split('$', 2)
    except (KeyError, ValueError):
        print(False)
    encoded = encode(password, salt, int(iterations))
    print(constant_time_compare(passwords[username], encoded))


def encode(password, salt, iterations):
    """Create an encoded value."""
    hash = pbkdf2(password, salt, iterations)
    hash = base64.b64encode(hash).decode('ascii').strip()
    return '%d$%s$%s' % (iterations, salt, hash)


def gen_salt(length=12):
    """Return a securely generated random string."""
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return ''.join(random.choice(allowed_chars) for i in range(length))


def pbkdf2(password, salt, iterations, dklen=0):
    """Implement PBKDF2 as defined in RFC 2898, section 5.2."""
    hlen = hashlib.sha1().digest_size
    if not dklen:
        dklen = hlen
    if dklen > (2 ** 32 - 1) * hlen:
        raise OverflowError('dklen too big')
    l = -(-dklen // hlen)
    r = dklen - (l - 1) * hlen

    hex_format_string = '%%0%ix' % (hlen * 2)

    inner, outer = hashlib.sha1(), hashlib.sha1()
    if len(password) > inner.block_size:
        password = hashlib.sha1(password).digest()
    password += '\x00' * (inner.block_size - len(password))
    inner.update(password.translate(hmac.trans_36))
    outer.update(password.translate(hmac.trans_5C))

    def F(i):
        u = salt + struct.pack('>I', i)
        result = 0
        for j in xrange(int(iterations)):
            dig1, dig2 = inner.copy(), outer.copy()
            dig1.update(u)
            dig2.update(dig1.digest())
            u = dig2.digest()
            result ^= int(binascii.hexlify(u), 16)
        return binascii.unhexlify((hex_format_string % result).encode('ascii'))

    T = [F(x) for x in range(1, l)]
    return ''.join(T) + F(l)[:r]


def constant_time_compare(val1, val2):
    """Return True if the two strings are equal, False otherwise.

    The time taken is independent of the number of characters that match.
    """
    if len(val1) != len(val2):
        return False
    result = 0
    for x, y in zip(val1, val2):
        result |= ord(x) ^ ord(y)
    return result == 0


def main():
    parser = argparse.ArgumentParser(
        description='PBKDF2 password encode and verify functions.')
    parser.add_argument('action', choices=['store', 'verify'], help='action')
    parser.add_argument('username', help='username')
    parser.add_argument('password', help='password to encode/verify')
    parser.add_argument('-i', '--iterations', type=int, default=12000,
                        help='number of PBKDF2 iterations (only for encode)')
    parser.add_argument('-f', '--file', default='passwd.json', help='path to passwords file')
    args = parser.parse_args()
    if args.action == 'store':
        store(args.username, args.password, args.iterations, args.file)
    else:
        verify(args.username, args.password, args.file)


if __name__ == '__main__':
    main()
