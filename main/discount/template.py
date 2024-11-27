pkgname = "discount"
pkgver = "3.0.0d"
pkgrel = 0
# build_style = "cmake"
# cmake_dir = "cmake"
build_style = "configure"
configure_script = "configure.sh"
configure_args = [
    "--container",
    "--cxx-binding",
    "--enable-all-features",
    "--mandir=/usr/share/man",
    "--pkg-config",
    "--prefix=/usr",
    "--shared",
]
make_dir = "."
make_install_target = "install.everything"
make_check_target = "test"
hostmakedepends = ["pkgconf"]
pkgdesc = "Markdown to HTML translator"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://www.pell.portland.or.us/~orc/Code/discount"
source = f"https://github.com/Orc/discount/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "0ed8cc27ac5d46dc6a8beedd5e5673ac8b466a6474bdb7d35f37c815f670385f"


def post_install(self):
    self.install_license("COPYRIGHT")


@subpackage("discount-devel")
def _(self):
    return self.default_devel()


@subpackage("discount-progs")
def _(self):
    return self.default_progs()
