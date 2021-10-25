import os
import secrets

import msal

from flask import Flask, request, flash, redirect,\
    url_for, render_template, session
from flask_login import LoginManager, current_user, UserMixin,\
    login_user, logout_user, login_required

app = Flask(__name__)

__all__ = ['login', 'logout']

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

client_id = os.environ.get('CLIENT_ID', None)
client_secret = os.environ.get('CLIENT_SECRET', None)
tenant_id = os.environ.get('TENANT_ID', None)

csrf_token = secrets.token_urlsafe()

authority = f'https://login.microsoftonline.com/{tenant_id}'

aad = msal.ConfidentialClientApplication(client_id,
                                         client_secret,
                                         authority)

class User(UserMixin):

    def __init__(self, user_id):
        global aad
        self.id = user_id
        print('account', aad.token_cache._cache)

    @property
    def username(self):
        return self.id.split('@')[0]
            
    @property
    def is_authenticated(self):
        global aad
        account = aad.get_accounts(self.id)
        print('is_authenticated', account)
        if account:
            return 'access_token' in aad.acquire_token_silent([], account[0])
        return False

@login_manager.user_loader
def load_user(user_id):
    print(user_id)
    return User(user_id)

@app.route('/login')
def login():

    if current_user.is_authenticated:
        return redirect(url_for('index'))

    
    code = request.args.get('code')
    if code:
        if request.args.get('state') != csrf_token:
            flash('CSRF error!')
            return(url_for('login'))
        response = aad.acquire_token_by_authorization_code(code,
                                                           [])
        if response and 'access_token' in response:
            user = User(response['id_token_claims']['preferred_username'])
            login_user(user)
            flash('Logged in successfully via AAD.')
            return redirect(url_for('index'))
        
    return redirect(aad.get_authorization_request_url([], state=csrf_token))

@app.route('/logout')
def logout():
    global aad
    account = aad.get_accounts(current_user.get_id())
    if account:
        aad.remove_account(account[0])
    logout_user()

    ms_uri = 'https://login.microsoftonline.com/common/oauth2/v2.0/logout'
    site = 'https://localhost:5050'
    
    return redirect(ms_uri+f'?post_logout_redirect_uri={site}'+url_for('index'))