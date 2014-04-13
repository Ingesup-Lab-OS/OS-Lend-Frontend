import yaml

class HeatTemplateHelper:
    def getDescription(document):
        print yaml.dump(yaml.load(document)