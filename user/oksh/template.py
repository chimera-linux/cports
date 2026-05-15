pkgname = "oksh"
pkgver = "7.8"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = []
make_dir = "."
makedepends = ["ncurses-devel"]
pkgdesc = "Portable OpenBSD ksh, based on pdksh"
license = "custom:none"
url = "https://github.com/ibara/oksh"
source = f"{url}/releases/download/oksh-{pkgver}/oksh-{pkgver}.tar.gz"
sha256 = "3b30d5a1183b829590cc020d8ab87f22d288e98dc3fdf12feb7159536beaa950"
hardening = ["vis", "cfi"]
# There are no tests
options = ["!check"]


def post_install(self):
    self.install_shell("/usr/bin/oksh")
