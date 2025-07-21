pkgname = "graphviz"
pkgver = "12.2.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-lefty"]
configure_gen = ["./autogen.sh"]
# otherwise y.tab.h is not located
make_dir = "."
make_install_args = ["-j1"]
hostmakedepends = [
    "automake",
    "bison",
    "flex",
    "libtool",
    "libtool-devel",
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
    "zlib-ng-compat-devel",
]
checkdepends = ["fonts-liberation-otf"]
depends = ["fonts-liberation"]
triggers = ["/usr/lib/graphviz"]
pkgdesc = "Graph visualization software"
license = "EPL-1.0"
url = "https://graphviz.org"
source = f"https://gitlab.com/graphviz/graphviz/-/archive/{pkgver}/graphviz-{pkgver}.tar.gz"
sha256 = "91d444b4dabdaf5bfa7c6fcc3a1ee5d41e588af6079ebc030f0acb79e48a56ea"
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
def _(self):
    return self.default_libs()


@subpackage("graphviz-devel")
def _(self):
    return self.default_devel()
