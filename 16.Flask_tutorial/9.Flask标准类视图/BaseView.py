from flask import Flask, render_template, views
from flask.typing import ResponseReturnValue

app = Flask(__name__)


class BaseView(views.View):
    def get_template(self):
        raise NotImplementedError()

    def get_date(self):
        raise NotImplementedError()

    def dispatch_request(self):
        data = self.get_date()
        template = self.get_template()
        return render_template(template, **data)
