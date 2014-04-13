import urllib2
import re
import subprocess
import commands
import os
import sys

from django.conf import settings

class HeatTemplateFetcher:
    CLONE_URL = 'https://github.com/Ingesup-Lab-OS/OS-Lend-Templates.git'
    HEAT_TEMPLATE_NAME = 'OS-Lend-Templates'
    HEAT_TEMPLATE_URL = 'https://github.com/Ingesup-Lab-OS/OS-Lend-Templates/commits/master'
    LAST_COMMIT_HASH_PATTERN = '<a href="/Ingesup-Lab-OS/OS-Lend-Templates/commit/(\w+)" class="gobutton ">'

    def __init__(self):
        self.remote_commit_hash = self.getRemoteCommitHash()
        self.heat_template_dir = settings.BASE_DIR+'/'+self.HEAT_TEMPLATE_NAME

    def getRemoteCommitHash(self):
        response = urllib2.urlopen(self.HEAT_TEMPLATE_URL)
        m = re.search(self.LAST_COMMIT_HASH_PATTERN, response.read())
        self.remote_commit_hash = m.group(1)
        return self.remote_commit_hash

    def getCurrentCommitHash(self):
        pr = subprocess.Popen( "/usr/bin/git log --pretty=format:'%H' -n 1" , cwd = self.heat_template_dir, shell = True,
            stdout = subprocess.PIPE, stderr = subprocess.PIPE )
        return pr.communicate()

    def clone(self):
        pr = subprocess.Popen( "/usr/bin/git clone "+ self.CLONE_URL, cwd = settings.BASE_DIR, shell = True,
            stdout = subprocess.PIPE, stderr = subprocess.PIPE )
        (out, error) = pr.communicate()

    def pull(self):
        pr = subprocess.Popen( "/usr/bin/git pull -u origin master", cwd = self.heat_template_dir, shell = True,
            stdout = subprocess.PIPE, stderr = subprocess.PIPE )
        (out, error) = pr.communicate()

    def startFetching(self):
        print 'Start fetching ', self.HEAT_TEMPLATE_NAME
        if not os.path.isdir(self.heat_template_dir):
            print "cloning ..."
            self.clone()
            print 'done'

        if not os.path.exists(self.heat_template_dir+"/.git"):
            print "no git found"
            import shutil
            shutil.rmtree(self.heat_template_dir)
            self.clone()

        (out, error) = self.getCurrentCommitHash()

        if not error:
            if not out == self.remote_commit_hash:
                print 'pulling repository...'
                pull()
            self.done()
        else:
            print error

    def done(self):
        print self.HEAT_TEMPLATE_NAME+' is up to date'

if __name__ == "__main__":
    fetcher = HeatTemplateFetcher()
    fetcher.startFetching()