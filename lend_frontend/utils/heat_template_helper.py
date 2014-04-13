import re
from string_helper import StringHelper

class HeatTemplateHelper:
    @staticmethod
    def getYamlFilesList(path):
        from glob import glob
        if path[-1] != '/':
            path += '/'
        return glob("%s*.yml" % path)

    @staticmethod
    def getTupleFromFile(file):
        """
        Get the file name in path and return a tuple
        with (filename, title)

        Ex : 
        /my/server/path/my-example_file-123.yml 
        give (my-example_file-123, my example file 123)

        """
        m =re.search('/OS-Lend-Templates/heat/(.*)\.yml', file)
        return (m.group(1), StringHelper.replace_all(m.group(1), { '-': ' ', '_': ' '}))

    @staticmethod
    def getAllTuplesFromPath(path):
        yamls = HeatTemplateHelper.getYamlFilesList(path)
        l = []
        for p in yamls:
            l.append(HeatTemplateHelper.getTupleFromFile(p))
        return tuple(l)

if __name__ == "__main__":
    v = 'oki'
    v2 = 'oki2'
    print "%s/%s" %(v, v2)
    yamls = HeatTemplateHelper.getYamlFilesList("../../OS-Lend-Templates/heat/")
    l = []
    for path in yamls:
        l.append(HeatTemplateHelper.getTupleFromFile(path))
    print tuple(l)
    print HeatTemplateHelper.getAllTuplesFromPath("../../OS-Lend-Templates/heat/")