from dash import html, page_container, dcc, page_registry, callback, Input, Output
from flask import session


def layout():
    test = html.Div(children=[
        html.Div(id="fire", children="Hello, world"),
        html.Div(id="navigation-links"),
        html.Div(page_container)])
    return test


@callback(
[Output('navigation-links', 'children')],
[Input('navigation-links', 'children')])
def update_user(children):
    try:
        user_name = session.get('user_name', None)
        project_name = session.get('project_name', None)
        links = []
        for page in page_registry.values():
            if "Home" in page['name']:
                links.append(dcc.Link(
                f"{page['name']} - {page['path']}", href=f"{page['relative_path']}"))
            else:
                links.append(dcc.Link(
                f"{page['name']} - {page['path']}", href=f"{page['relative_path']}/{user_name}/{project_name}"))
        return [html.Div(links)]
    except:
        return -10