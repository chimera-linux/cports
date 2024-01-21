pkgname = "oksh"
pkgver = "7.4"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = []
makedepends = ["ncurses-devel"]
pkgdesc = "Portable OpenBSD ksh, based on the Public Domain Korn Shell (pdksh)"
maintainer = "ttyyls <contact@behri.org>"
license = "custom:none"
url = "https://github.com/ibara/oksh"
source = f"{url}/releases/download/{pkgname}-{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "be9a8d457bf373bd04618074c41b46f4edec2ba1c57a58be881d60eaa6628596"
hardening = ["vis", "cfi"]
# There are no tests
options = ["!check"]


def do_install(self):
    self.install_bin("build/oksh")
    self.install_man("ksh.1")
    self.install_man("oksh.1")


def post_install(self):
    self.install_shell("/usr/bin/oksh")
