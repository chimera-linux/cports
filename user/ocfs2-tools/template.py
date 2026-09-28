pkgname = "ocfs2-tools"
pkgver = "1.8.9"
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
license = "GPL-2.0-only"
url = "https://github.com/markfasheh/ocfs2-tools"
source = f"{url}/archive/refs/tags/ocfs2-tools-{pkgver}.tar.gz"
sha256 = "044bdd7c18c88f79e7a0352c92e8071968fe8460cec749b06653ded57a693d51"
tool_flags = {"CFLAGS": ["-Dloff_t=off_t"]}
# no tests
options = ["!check"]


def post_install(self):
    # static libs only and not used by anything
    self.uninstall("usr/include")
    self.uninstall("usr/lib")
