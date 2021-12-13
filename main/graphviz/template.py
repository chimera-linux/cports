pkgname = "graphviz"
pkgver = "2.50.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-lefty"
]
make_cmd = "gmake"
# otherwise y.tab.h is not located
make_dir = "."
make_install_args = ["-j1"]
hostmakedepends = [
    "gmake", "pkgconf", "automake", "libtool", "libltdl-devel", "flex",
    "bison", "perl", "python"
]
makedepends = [
    "libpng-devel", "libjpeg-turbo-devel", "libwebp-devel", "libgd-devel",
    "zlib-devel", "libexpat-devel", "fontconfig-devel", "cairo-devel",
    "pango-devel", "freetype-devel",
]
checkdepends = ["fonts-liberation-otf"]
depends = ["virtual:fonts-liberation"]
depends_providers = {
    "virtual:fonts-liberation": "fonts-liberation-otf"
}
triggers = ["/usr/lib/graphviz"]
pkgdesc = "Graph visualization software"
maintainer = "q66 <q66@chimera-linux.org>"
license = "EPL-1.0"
url = "https://graphviz.org"
source = f"https://gitlab.com/{pkgname}/{pkgname}/-/archive/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "afa48581f764a35e148909cc96a0308ec2356b5225b64af12492f3392f20ef1c"
# expects already installed graphviz
# testing is via pytest
options = ["!check"]

def init_configure(self):
    self.make_build_args += ["HOSTCC=" + self.get_tool("CC")]

def pre_configure(self):
    self.do(self.chroot_cwd / "autogen.sh")

def post_install(self):
    self.install_license("epl-v10.txt")

    self.rm(self.destdir / "usr/share/graphviz/doc", recursive = True)
    # not built
    self.rm(self.destdir / "usr/share/man/man1/mingle.1")
    # useless
    self.rm(self.destdir / "usr/bin/dot_builtins")

@subpackage("graphviz-libs")
def _libs(self):
    return self.default_libs()

@subpackage("graphviz-devel")
def _devel(self):
    return self.default_devel(man = True)
