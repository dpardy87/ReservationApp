# pylint:disable=invalid-name, wrong-import-position, no-member, import-error, broad-except
"""entrypoint for application"""
import os
import sys
from flask import Flask, render_template
from adapters.sql_adapter import SqlAdapter
from handler import ReservationHandler

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + "/../conf/")
import config

app = Flask(__name__)


def get_handler():
    """returns handler obj"""
    sql_adapter = SqlAdapter(app.config.get("PGSQL_CONN_STR"))
    handler = ReservationHandler(
        sql_adapter=sql_adapter
    )
    return handler

@app.route("/")
def home():
    """docstring for home"""
    return render_template("home.html")


@app.route("/about")
def about():
    """docstring for about"""
    return "This is the about page"


def load_config(env):
    """load_config docstring"""
    config_map = {"dev": config.DevelopmentConfig().serialize()}

    # get config based on env parameter
    selected_config = config_map.get(env)

    if not selected_config:
        raise ValueError(
            f"Invalid environment '{env}'. Expected one of {list(config_map.keys())}."
        )

    app.config.update(
        {key: value for key, value in selected_config.items() if key.isupper()}
    )

    # set debug flag, default to false
    app.debug = selected_config.get("DEBUG", False)


if __name__ == "__main__":
    # just hardcode to dev for the time being
    environment = "dev"
    load_config(environment)
    app.run(host="0.0.0.0", port=5000, debug=app.debug)
