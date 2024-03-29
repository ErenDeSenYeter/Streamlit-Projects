import plotly.graph_objects as go

fig = go.Figure(go.Scattermapbox(
    fill = "toself",
    lon = [-74, -70, -70, -74], lat = [47, 47, 45, 45],
    marker = { 'size': 10, 'color': "orange" }))

fig.update_layout(
    mapbox = {
        'style': "open-street-map",
        'center': {'lon': -73, 'lat': 46 },
        'zoom': 5},
    showlegend = False)

fig.show()