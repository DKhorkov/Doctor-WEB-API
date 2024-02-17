from flask import Flask

from .views import upload_view, param_download_view, query_download_view, query_delete_view, param_delete_view
from .configs import Methods, URLRules, URLNames


app: Flask = Flask(__name__)

app.add_url_rule(
    rule=URLRules.upload.value,
    view_func=upload_view,
    methods=[Methods.post.value, Methods.options.value],
    endpoint=URLNames.upload.value
)

app.add_url_rule(
    rule=URLRules.query_download.value,
    view_func=query_download_view,
    methods=[Methods.get.value, Methods.options.value],
    endpoint=URLNames.query_download.value
)

app.add_url_rule(
    rule=URLRules.param_download.value,
    view_func=param_download_view,
    methods=[Methods.get.value, Methods.options.value],
    endpoint=URLNames.param_download.value
)

app.add_url_rule(
    rule=URLRules.query_delete.value,
    view_func=query_delete_view,
    methods=[Methods.delete.value, Methods.options.value],
    endpoint=URLNames.query_delete.value
)

app.add_url_rule(
    rule=URLRules.param_delete.value,
    view_func=param_delete_view,
    methods=[Methods.delete.value, Methods.options.value],
    endpoint=URLNames.param_delete.value
)


if __name__ == "__main__":
    app.run()
