from flask import Flask

from .views import homepage_view, upload_view
from .configs import Methods, URLRules, URLNames


app: Flask = Flask(__name__)

app.add_url_rule(
    rule=URLRules.homepage.value,
    view_func=homepage_view,
    methods=[Methods.get.value, Methods.options.value],
    endpoint=URLNames.homepage.value
)

app.add_url_rule(
    rule=URLRules.upload.value,
    view_func=upload_view,
    methods=[Methods.post.value, Methods.options.value],
    endpoint=URLNames.upload.value
)


if __name__ == '__main__':
    app.run()
