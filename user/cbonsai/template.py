pkgname = "cbonsai"
pkgver = "1.4.2"
pkgrel = 0
build_style = "makefile"
makedepends = ["ncurses-devel", "ncurses-libtinfo-devel"]
pkgdesc = "Console-based Bonsai tree visualiser"
license = "GPL-3.0-or-later"
url = "https://gitlab.com/jallbrit/cbonsai"
source = f"{url}/-/archive/v{pkgver}/cbonsai-v{pkgver}.tar.gz"
sha256 = "75cf844940e5ef825a74f2d5b1551fe81883551b600fecd00748c6aa325f5ab0"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
