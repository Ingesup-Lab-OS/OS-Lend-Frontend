import re
from string_helper import StringHelper
from django.conf import settings

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

    @staticmethod
    def get_full_path_from_file_name(file_name):
        full_path = '%s/%s.yml' %(settings.FULL_TEMPLATE_FOLDER, file_name)
        from os.path import exists
        if exists(full_path):
            return full_path

        raise ValueError('Le template yaml est introuvable.')