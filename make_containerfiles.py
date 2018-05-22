#!/usr/bin/env python
import jinja2


CONTAINER_FILENAME = {
    'singularity': 'Singularity',
    'docker': 'Dockerfile',
}


def main():
    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader('templates'),
        trim_blocks=True)

    for container_system in sorted(CONTAINER_FILENAME):
        template = env.get_template(container_system + '.jinja')
        for cuda in (False, True):
            for system in ('flux', 'comet', 'bridges'):

                image = 'glotzerlab/software'
                fn = CONTAINER_FILENAME[container_system]

                tag = 'cuda8-' + system if cuda else system
                if tag:
                    image += ':' + tag
                    fn += '.' + tag

                recipe = template.render({'base_image': image, 'cuda': cuda})
                print("Writing '{}'.".format(fn))
                with open(fn, 'w') as containerfile:
                    containerfile.write(recipe + '\n')


if __name__ == '__main__':
    main()
