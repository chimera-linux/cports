pkgname = "eventlog"
pkgver = "0.2.13"
pkgrel = 0
_commit = "a5c19163ba131f79452c6dfe4e31c2b4ce4be741"
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "automake", "libtool"]
pkgdesc = "API to format and send structured log messages"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://github.com/balabit/eventlog"
source = f"{url}/archive/{_commit}.tar.gz"
sha256 = "ddd8c19cf70adced542eeb067df275cb2c0d37a5efe1ba9123102eb9b4967c7b"


def post_install(self):
    self.install_license("COPYING")


@subpackage("eventlog-devel")
def _devel(self):
    return self.default_devel()
