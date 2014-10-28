# -*- coding: utf-8 -*-
"""Jinja2 filters for Postgresql config files."""
MULTIPLES = (
    ('GB', 1024 ** 3),
    ('MB', 1024 ** 2),
    ('kB', 1024 ** 1),
    ('', 1024 ** 0)
)


def pg_size(size):
    """Return string representation of memory size."""
    for suffix, factor in MULTIPLES:
        if size >= factor * 10:
            break
    amount = int(size / factor)
    return str(amount) + suffix


def shared_buffers(mem):
    """Calculate shared_buffers size in bytes."""
    return mem // 4


def pg_shared_buffers(mem):
    """Calculate shared_buffers size."""
    return pg_size(shared_buffers(mem))


def pg_work_mem(mem, max_connections=200):
    """Calculate work_mem size."""
    return pg_size((mem - shared_buffers(mem)) // (max_connections * 3))


def pg_maintenance_work_mem(mem):
    """Calculate maintenance_work_mem size."""
    return pg_size(min(mem // 16, 2 * 1024 ** 3))


def pg_effective_cache_size(mem):
    """Calculate effective_cache_size."""
    return pg_size((mem * 3) // 4)


def pg_wal_buffers(mem):
    """Calculate wal_buffers size."""
    wal_buffers = min((shared_buffers(mem) * 3) // 100, 16 * 1024 ** 2)
    if wal_buffers > 14 * 1024 ** 2:
        wal_buffers = 16 * 1024 ** 2
    return pg_size(wal_buffers)


class FilterModule(object):

    """Jinja2 filters for Postgresql config files."""

    def filters(self):
        """Return filter functions."""
        return {
            'pg_size': pg_size,
            'pg_shared_buffers': pg_shared_buffers,
            'pg_work_mem': pg_work_mem,
            'pg_maintenance_work_mem': pg_maintenance_work_mem,
            'pg_effective_cache_size': pg_effective_cache_size,
            'pg_wal_buffers': pg_wal_buffers,
        }
