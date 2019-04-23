import json
import random

from jinja2 import Template


def main():
    data = usgs_data()
    # Sort the data and segregate "large" earthquakes
    # measuring 5.0 magnitude or greater.
    all_quakes = sort_quakes(data)
    large_quakes = []
    for quake in all_quakes:
        if quake['properties']['mag'] >= 5:
            large_quakes.append(quake)

    # TODO: You must create a Jinja template called 'story_template.html'
    # in the root of this repo that generates the expected output.
    raw_template = story_template()
    t = Template(raw_template)

    kwargs = {
        'title': 'Daily earthquake report',
        #TODO: Experiment with different hard-coded values
        # to ensure your template logic works for all scenarios!
        'num_large_quakes_yesterday': random.randint(5,10),
        'large_quakes': large_quakes[0:5],
        'large_quakes_count': len(large_quakes),
        'num_quakes': len(data),
    }
    # Render the template
    compiled_text = t.render(**kwargs)
    # Write the template to a local file called daily_quake_alert.html
    write_story(compiled_text)

def story_template():
    with open('story_template.html') as f:
        return f.read()

def sort_quakes(earthquakes):
    return sorted(
        earthquakes,
        key=lambda x: x['properties']['mag'],
        reverse=True
    )

def usgs_data():
    with open('usgs_all_day.geojson') as f:
        return json.load(f)['features']

def write_story(text):
    with open('daily_quake_alert.html', 'w') as f:
        f.write(text)


if __name__ == '__main__':
    main()
