pkgname = "gpm"
pkgver = "1.20.7"
pkgrel = 3
build_style = "gnu_configure"
configure_args = ["--disable-static"]
configure_gen = ["./autogen.sh"]
make_dir = "."
hostmakedepends = [
    "automake",
    "bison",
    "flex",
    "libtool",
    "texinfo",
]
makedepends = [
    "dinit-chimera",
    "flex-devel-static",
    "linux-headers",
    "ncurses-devel",
]
depends = ["cmd:pgrep!procps"]
pkgdesc = "Mouse server for the console"
license = "GPL-2.0-or-later"
url = "https://www.nico.schottelius.org/software/gpm"
source = f"{url}/archives/gpm-{pkgver}.tar.gz"
sha256 = "c7e4661c24e05ae13547176b649bac8e3a0db2575f7dd57559f9e0b509f90f49"
# no tests
options = ["!check"]


def post_install(self):
    self.install_link("usr/lib/libgpm.so", "libgpm.so.2.1.0")
    self.install_service(self.files_path / "gpm")
    self.install_file(self.files_path / "gpm.sh", "etc/profile.d")


@subpackage("gpm-devel")
def _(self):
    return self.default_devel()


@subpackage("gpm-libs")
def _(self):
    return self.default_libs()
