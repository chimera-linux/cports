pkgname = "graphviz"
pkgver = "11.0.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-lefty"]
configure_gen = ["./autogen.sh"]
make_cmd = "gmake"
# otherwise y.tab.h is not located
make_dir = "."
make_install_args = ["-j1"]
hostmakedepends = [
    "automake",
    "bison",
    "flex",
    "gmake",
    "libltdl-devel",
    "libtool",
    "perl",
    "pkgconf",
    "python",
]
makedepends = [
    "cairo-devel",
    "fontconfig-devel",
    "freetype-devel",
    "gdk-pixbuf-devel",
    "libexpat-devel",
    "libgd-devel",
    "libjpeg-turbo-devel",
    "libpng-devel",
    "libwebp-devel",
    "pango-devel",
    "zlib-devel",
]
checkdepends = ["fonts-liberation-otf"]
depends = ["fonts-liberation"]
triggers = ["/usr/lib/graphviz"]
pkgdesc = "Graph visualization software"
maintainer = "q66 <q66@chimera-linux.org>"
license = "EPL-1.0"
url = "https://graphviz.org"
source = f"https://gitlab.com/graphviz/graphviz/-/archive/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "d374f7d98a1ae985510a82dddd887e8058aa37e5f95b4ce0aa58416d2b22714b"
# expects already installed graphviz
# testing is via pytest
options = ["!check"]


def init_configure(self):
    self.make_build_args += ["HOSTCC=" + self.get_tool("CC")]


def post_install(self):
    self.install_license("epl-v10.txt")
    # useless
    self.rm(self.destdir / "usr/bin/dot_builtins")


@subpackage("graphviz-libs")
def _libs(self):
    return self.default_libs()


@subpackage("graphviz-devel")
def _devel(self):
    return self.default_devel()
