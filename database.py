import os
import streamlit_authenticator as stauth
from deta import Deta  # pip install deta


# Load the environment variables

DETA_KEY = "d0jg2qpgu33_xzNNgZcz1ZBM1WMDTXta3uuq6zzqVZKj"


# Initialize with a project key
deta = Deta(DETA_KEY)

# This is how to create/connect a database
db = deta.Base("users_db")


def insert_user(username, name, password):
    """Returns the user on a successful user creation, otherwise raises and error"""
    return db.put({"key": username, "name": name, "password": password})


def fetch_all_users():
    """Returns a dict of all users"""
    res = db.fetch()
    return res.items


def get_user(username):
    """If not found, the function will return None"""
    return db.get(username)


def update_user(username, updates):
    """If the item is updated, returns None. Otherwise, an exception is raised"""
    return db.update(updates, username)


def delete_user(username):
    """Always returns None, even if the key does not exist"""
    return db.delete(username)
