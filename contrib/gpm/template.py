pkgname = "gpm"
pkgver = "1.20.7"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-static"]
configure_gen = ["./autogen.sh"]
make_cmd = "gmake"
make_dir = "."
hostmakedepends = ["automake", "gmake", "libtool", "texinfo", "flex", "bison"]
makedepends = [
    "linux-headers",
    "ncurses-devel",
    "libfl-devel-static",
]
depends = ["cmd:pgrep!procps"]
pkgdesc = "Mouse server for the console"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://www.nico.schottelius.org/software/gpm"
source = f"{url}/archives/gpm-{pkgver}.tar.gz"
sha256 = "c7e4661c24e05ae13547176b649bac8e3a0db2575f7dd57559f9e0b509f90f49"
# no tests
options = ["!check"]


def post_install(self):
    self.install_link("libgpm.so.2.1.0", "usr/lib/libgpm.so")
    self.install_service(self.files_path / "gpm")
    self.install_file(self.files_path / "gpm.sh", "etc/profile.d")


@subpackage("gpm-devel")
def _devel(self):
    return self.default_devel()


@subpackage("gpm-libs")
def _libs(self):
    return self.default_libs()
