from presenter.dash_app import *
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from flask import session


class LoginPt(object):
    def set_layout(self):
        return dbc.Form([
            dbc.Row(
                [
                    dbc.Label("User", html_for="user_row", width=2),
                    dbc.Col(
                        dbc.Input(id="user_row", placeholder="Enter user"),
                        width=10,
                    ),
                    dbc.Input(id="rs", placeholder="test1"),
                    dbc.Input(id="rs2", placeholder="test2"),
                ],
                className="mb-3",
            ),
            dbc.Row(
                [
                    dbc.Label("Password", html_for="password_row", width=2),
                    dbc.Col(
                        dbc.Input(
                            type="password",
                            id="password_row",
                            placeholder="Enter password",
                        ),
                        width=10,
                    ),
                ],
                className="mb-3",
            ),
            dbc.Row([
                dbc.Button("Login", color="secondary", id='login_button', className="me-1"),
            ]),
        ])

    def render(self):
        @app.callback(
            [Output("rs", "value")],
            [Input("user_row", "value"), Input("password_row", "value")],
        )
        def check_validity(user_name, pwd):
            if user_name:
                return "True"
            return "False"

        @app.callback(Output("rs2", "value"), [Input("user_row", "value"), Input("password_row", "value")])
        def set_session(v1, v2):
            session['username'] = v1
            session['password'] = v2
            return "vvvvvvv"
