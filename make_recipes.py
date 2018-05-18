import os
import glob
import jinja2


TEMPLATES = {
    'singularity.jinja': 'Singularity',
    'docker.jinja': 'Dockerfile',
}


if __name__ == '__main__':
    env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))

    # Docker
    template = env.get_template('docker.jinja')
    image = 'glotzerlab/software:latest'
    recipe = template.render({'base_image': image})
    print("Building '{}'...".format('Dockerfile'))
    with open('Dockerfile', 'w') as dockerfile:
        dockerfile.write(recipe + '\n')

    # Singularity
    template = env.get_template('singularity.jinja')
    for cuda in (False, True):
        for system in ('flux', 'comet', 'bridges'):
            tag = 'cuda8-' + system if cuda else system
            image = 'glotzerlab/software:' + tag
            fn = 'Singularity.' + tag
            print("Building '{}'...".format(image))
            recipe = template.render({'base_image': image})
            with open(fn, 'w') as recipe_file:
                recipe_file.write(recipe + '\n')
