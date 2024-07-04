pkgname = "libvisual"
pkgver = "0.4.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-examples", "--disable-lv-tool"]
make_cmd = "gmake"
# must be used to overwrite generated junk that messes up build
make_dir = "."
hostmakedepends = [
    "autoconf-archive",
    "automake",
    "gettext-devel",
    "gmake",
    "libtool",
    "pkgconf",
]
pkgdesc = "Abstraction library for audio visualization plugins"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "http://libvisual.org"
source = f"https://github.com/Libvisual/libvisual/releases/download/libvisual-{pkgver}/libvisual-{pkgver}.tar.gz"
sha256 = "63085fd9835c42c9399ea6bb13a7ebd4b1547ace75c4595ce8e9759512bd998a"


def post_install(self):
    self.uninstall("usr/share/man/man1/lv-tool-0.4.1")


@subpackage("libvisual-devel")
def _devel(self):
    return self.default_devel()
