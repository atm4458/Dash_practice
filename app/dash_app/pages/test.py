from dash import register_page, html, callback, Input, Output, dcc, MATCH, ALL

# register_page(__name__, path="/test", title="Test1_App")
register_page(__name__, path="/test",
              path_template="/test/<user_name>/<project_name>", title="Test1_App")

sub_calss_in_row = 3

def layout(user_name=None, project_name=None):
    content = html.Div([html.Div("this is test.py. {}/{}".format(user_name, project_name)),
                        html.Div(html.Button("Add Row",
                                 id="add-figure", n_clicks=0)),
                        html.Div([], id="work-space-test", className="container")])
    return content


@callback(Output(component_id="work-space-test", component_property="children"),
          Input(component_id="add-figure", component_property="n_clicks"),
          Input(component_id="work-space-test", component_property="children"), prevent_initial_call=True)
def add_figure(n_click, original_component):
    component_list = original_component
    start_index = len(component_list)*sub_calss_in_row
    row_component = []
    for index in range(sub_calss_in_row):
        curr_index = start_index + index + 1
        print(curr_index)
        row_component.append(create_component(curr_index))

    component_list.append(html.Div(children=row_component, className="row"))
    return component_list





def create_component(index):
    pickle_button = dcc.Dropdown(
        ["0", "1", "2"], id={"type": "test-pickle-list", "index": index}, placeholder="Pickle name")
    lot_lists = dcc.Dropdown(multi=True, id={
                             "type": "test-lot-list", "index": index}, placeholder="Lot name")
    chain_lists = dcc.Dropdown(multi=True, id={
                             "type": "test-chain-list", "index": index}, placeholder="Chain name")
    wafer_map = dcc.Graph(id={"type": "test-wafer-map", "index": index})
    pchart = dcc.Graph(id={"type": "test-pchart", "index": index})
    content = [html.Div(item)
               for item in [pickle_button, lot_lists, chain_lists, wafer_map, pchart]]
    return html.Div(content, className="col", style={"width":"200px"})


@callback(Output(component_id={"type": "test-lot-list", "index": MATCH}, component_property="options"),
          Input(component_id={"type": "test-pickle-list", "index": MATCH}, component_property="value"), prevent_initial_call=True)
def update_lot_list(value):
    print(value, type(value))
    if value is None: return None
    candidate_options = {"0": ["a", "b", "c"],
                        "1": ["d", "e", "f"],
                        "2": ["g", "h", "i"]}
    return candidate_options[value]