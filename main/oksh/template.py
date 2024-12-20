pkgname = "oksh"
pkgver = "7.6"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = []
make_dir = "."
makedepends = ["ncurses-devel"]
pkgdesc = "Portable OpenBSD ksh, based on pdksh"
maintainer = "ttyyls <contact@behri.org>"
license = "custom:none"
url = "https://github.com/ibara/oksh"
source = f"{url}/archive/refs/tags/oksh-{pkgver}.tar.gz"
sha256 = "159fb914694d6f14d23eb87ecb551b42d4356907820e5cc1cc8c327dc5c24c6a"
hardening = ["vis", "cfi"]
# There are no tests
options = ["!check"]


def post_install(self):
    self.install_shell("/usr/bin/oksh")
