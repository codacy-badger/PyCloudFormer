import yaml
from jinja2 import Environment, FileSystemLoader


class YamlBuilder:
    """
    Class designed to generate AWS Cloud Formation templates with relative files and configs
    """

    def __init__(self, configs, template, output):
        self.configs = configs
        self.template = template
        self.output = output

    @staticmethod
    def load_yaml(e):
        """
        loads yaml into a python dictionary
        :param e: yaml file directory
        :return: dictionary
        """
        return yaml.load(open(e), yaml.FullLoader)

    def build_yaml(self):
        """
        collects configs and templates to generate a yaml file
        :return: writes a yaml file in the output directory
        """
        config_data = self.load_yaml(self.configs)
        env = Environment(loader=FileSystemLoader('./'), trim_blocks=True, lstrip_blocks=True)
        template = env.get_template(self.template)
        print(template.render(config_data), file=open(self.output, "w"))





