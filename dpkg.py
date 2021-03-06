import shutil
import subprocess
import dotbot

from os.path import expanduser


class Dpkg(dotbot.Plugin):
    _directive_dpkg = "dpkg"

    def can_handle(self, directive):
        return directive == self._directive_dpkg

    def handle(self, directive, data):
        self._gdebi = shutil.which("dpkg")
        if not isinstance(data, list):
            self._log.error("Error format, please refer to docs.")
            return False
        return self._handle_deb(data)

    def _handle_deb(self, data):
        for package in data:
            if package.startswith('~'):
                package = expanduser(package)
            subprocess.call(["dpkg", "-i", package])
        subprocess.call(["apt", "install", "-f", "-y"])
        return True
