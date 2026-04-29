"""
SQLite database file initializer.

This module only creates the local SQLite file (default: `notic.db`).
"""

from __future__ import annotations

import os
import sqlite3
from typing import Optional


DEFAULT_DB_FILENAME = "notic.db"


def default_db_path() -> str:
    return os.path.join(os.path.dirname(__file__), DEFAULT_DB_FILENAME)


def get_connection(db_path: Optional[str] = None) -> sqlite3.Connection:
    path = db_path or default_db_path()
    conn = sqlite3.connect(path)
    return conn


def init_db(db_path: Optional[str] = None) -> str:
    """
    Create the SQLite database file (idempotent).

    Returns the absolute path to the database file.
    """
    path = db_path or default_db_path()
    with get_connection(path) as conn:
        conn.commit()
    return os.path.abspath(path)


if __name__ == "__main__":
    created_path = init_db()
    print(f"SQLite database initialized at: {created_path}")

