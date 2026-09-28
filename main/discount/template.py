pkgname = "discount"
pkgver = "3.0.1.2"
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
license = "BSD-3-Clause"
url = "https://www.pell.portland.or.us/~orc/Code/discount"
source = f"https://github.com/Orc/discount/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "4ea6cc8782c6508b3051c469ed7a1b6ca20b023c2a0c26ccd9c83bc7e61dfc16"


def post_install(self):
    self.install_license("COPYRIGHT")


@subpackage("discount-devel")
def _(self):
    return self.default_devel()


@subpackage("discount-progs")
def _(self):
    return self.default_progs()
