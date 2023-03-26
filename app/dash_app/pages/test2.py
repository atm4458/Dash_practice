from dash import register_page, html

# register_page(__name__, path="/test2", title="Test2_App")
register_page(__name__, path="/test2", path_template="/test2/<user_name>/<project_name>", title="Test2_App")

def layout(user_name=None, project_name=None):
    content = html.Div("this is test2.py. {}/{}".format(user_name, project_name))
    return content