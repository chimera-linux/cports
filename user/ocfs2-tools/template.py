pkgname = "ocfs2-tools"
pkgver = "1.8.8"
pkgrel = 0
build_style = "gnu_configure"
make_dir = "."
hostmakedepends = ["automake", "libtool", "pkgconf"]
makedepends = [
    "e2fsprogs-devel",
    "glib-devel",
    "libaio-devel",
    "libedit-readline-devel",
    "linux-headers",
    "ncurses-devel",
]
pkgdesc = "OCFS2 utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "https://github.com/markfasheh/ocfs2-tools"
source = f"{url}/archive/refs/tags/ocfs2-tools-{pkgver}.tar.gz"
sha256 = "675b967bf209d8a2b5aeb2bfb637e0c3001cd4dc5d812129c53a566cabc2958d"
tool_flags = {"CFLAGS": ["-Dloff_t=off_t"]}
# no tests
options = ["!check"]


def post_install(self):
    # static libs only and not used by anything
    self.uninstall("usr/include")
    self.uninstall("usr/lib")
