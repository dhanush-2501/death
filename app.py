
import streamlit as st
import streamlit_authenticator as stauth
from death_clock import death_clock
import database as db


users = db.fetch_all_users()

usernames = [user["key"] for user in users]
names = [user["name"] for user in users]
hashed_passwords = [user["password"] for user in users]

credentials = {"usernames":{}}

for un, name, pw in zip(usernames, names, hashed_passwords):
    user_dict = {"name":name,"password":pw}
    credentials["usernames"].update({un:user_dict})

authenticator = stauth.Authenticate(credentials, "death_clock", "abcdef", 3, "abc@gmail.com")

name, authentication_status, username = authenticator.login('Login', 'main')

if authentication_status:
    authenticator.logout('Logout', 'sidebar')
    st.write(f'Welcome *{name}*')
    death_clock()
    

elif authentication_status is False:
    st.error('Username/password is incorrect')
    try:
        if authenticator.reset_password(username, 'Reset password'):
            st.success('Password modified successfully')
    except Exception as e:
        st.error(e)

elif authentication_status is None:
    st.warning('Please enter your username and password')
