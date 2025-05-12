pkgname = "oksh"
pkgver = "7.7"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = []
make_dir = "."
makedepends = ["ncurses-devel"]
pkgdesc = "Portable OpenBSD ksh, based on pdksh"
license = "custom:none"
url = "https://github.com/ibara/oksh"
source = f"{url}/archive/refs/tags/oksh-{pkgver}.tar.gz"
sha256 = "c78684a4d0e1d4b828b9b5f4d53aab54eed692a281b81be6d7e2e81d0ce8ae6a"
hardening = ["vis", "cfi"]
# There are no tests
options = ["!check"]


def post_install(self):
    self.install_shell("/usr/bin/oksh")
