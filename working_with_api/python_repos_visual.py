import requests

from plotly.graph_objs import Bar
from plotly import offline


# Make an API call and store the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Process results.
response_dict = r.json()
repo_dicts = response_dict['items']
repo_links, stars, labels = [], [], []
for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    repo_url = repo_dict['url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)

    stars.append(repo_dict['stargazers_count'])

    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f"{owner}<br />{description}"
    labels.append(label)

# Make a visualization
data = [{
    'type': 'bar',
    'x': repo_links,
    'y': stars,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6,
}]

my_layout = {
    'title': 'Most-Starrred Python Projects on GitHub',
    'titlefont': {'size': 28, 'family': 'Times New Roman'},
    'xaxis': {
        'title': 'Repository',
        'titlefont': {'size': 24, 'family': 'Times New Roman'},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'Stars',
        'titlefont': {'size': 24, 'family': 'Times New Roman'},
        'tickfont': {'size': 14, 'family': 'Times New Roman'},
    },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='working_with_api/python_repos.html')