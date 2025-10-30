import reflex as rx
import sqlite3
import bcrypt
import os
from typing import Literal, Any, Optional, TypedDict

DATABASE_URL = "database.db"
Role = Literal["student", "professor", "admin"]


class User(TypedDict):
    id: int
    name: str
    email: str | None
    username: str | None
    university_id: str | None
    password_hash: str
    role: Role
    created_at: str


def get_db_connection():
    conn = sqlite3.connect(DATABASE_URL)
    conn.row_factory = sqlite3.Row
    return conn


def create_tables():
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE,
            username TEXT UNIQUE,
            university_id TEXT UNIQUE,
            password_hash TEXT NOT NULL,
            role TEXT NOT NULL CHECK(role IN ('student', 'professor', 'admin')),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """)
        conn.commit()


def _create_admin_user():
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM users WHERE username = ? AND role = 'admin'", ("admin",)
        )
        if cursor.fetchone() is None:
            password = "admin123"
            hashed_password = bcrypt.hashpw(
                password.encode("utf-8"), bcrypt.gensalt()
            ).decode("utf-8")
            cursor.execute(
                """
            INSERT INTO users (name, username, password_hash, role) 
            VALUES (?, ?, ?, ?)
            """,
                ("Admin User", "admin", hashed_password, "admin"),
            )
            conn.commit()
            print("Admin user created.")


create_tables()
_create_admin_user()


def create_user(
    name: str,
    password: str,
    role: Role,
    email: Optional[str] = None,
    username: Optional[str] = None,
    university_id: Optional[str] = None,
) -> int:
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode(
        "utf-8"
    )
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
        INSERT INTO users (name, email, username, university_id, password_hash, role)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
            (name, email, username, university_id, hashed_password, role),
        )
        conn.commit()
        return cursor.lastrowid


def get_user_by_email(email: str) -> Optional[User]:
    with get_db_connection() as conn:
        user = conn.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()
        return dict(user) if user else None


def get_user_by_username(username: str) -> Optional[User]:
    with get_db_connection() as conn:
        user = conn.execute(
            "SELECT * FROM users WHERE username = ?", (username,)
        ).fetchone()
        return dict(user) if user else None


def get_user_by_university_id(university_id: str) -> Optional[User]:
    with get_db_connection() as conn:
        user = conn.execute(
            "SELECT * FROM users WHERE university_id = ?", (university_id,)
        ).fetchone()
        return dict(user) if user else None


def verify_password(stored_hash: str, provided_password: str) -> bool:
    return bcrypt.checkpw(
        provided_password.encode("utf-8"), stored_hash.encode("utf-8")
    )


def authenticate_user(identifier: str, password: str, role: Role) -> Optional[User]:
    user = None
    if role == "student":
        user = get_user_by_university_id(identifier)
    elif role in ["professor", "admin"]:
        user = get_user_by_username(identifier)
    if user and verify_password(user["password_hash"], password):
        return user
    return None