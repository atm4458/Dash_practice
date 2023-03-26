from dash import register_page, html

register_page(__name__, path="/", title="Home")
# register_page(__name__, path="/test", path_template="/test/<user_name>/<project_name>", title="Test1_App")

def layout(user_name=None, project_name=None):
    content = html.Div("Home.py")
    return content