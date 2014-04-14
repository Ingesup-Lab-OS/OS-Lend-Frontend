import re
from string_helper import StringHelper

class HeatTemplateHelper:
    @staticmethod
    def get_yaml_files_list(path):
        from glob import glob
        if path[-1] != '/':
            path += '/'
        return glob("%s*.yml" % path)

    @staticmethod
    def get_tuple_fromfile(file):
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
    def get_all_tuples_from_path(path):
        yamls = HeatTemplateHelper.get_yaml_files_list(path)
        l = []
        for p in yamls:
            l.append(HeatTemplateHelper.get_tuple_fromfile(p))
        return tuple(l)

if __name__ == "__main__":
    v = 'oki'
    v2 = 'oki2'
    print "%s/%s" %(v, v2)
    yamls = HeatTemplateHelper.get_yaml_files_list("../../OS-Lend-Templates/heat/")
    l = []
    for path in yamls:
        l.append(HeatTemplateHelper.get_tuple_fromfile(path))
    print tuple(l)
    print HeatTemplateHelper.get_all_tuples_from_path("../../OS-Lend-Templates/heat/")