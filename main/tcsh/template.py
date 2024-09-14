pkgname = "tcsh"
pkgver = "6.24.13"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-nls"]
hostmakedepends = ["automake"]
makedepends = ["ncurses-devel"]
pkgdesc = "Enhanced version of the Berkeley UNIX C shell"
maintainer = "tulilirockz <tulilirockz@outlook.com>"
license = "BSD-2-Clause"
url = "https://astron.com/pub/tcsh"
source = f"{url}/tcsh-{pkgver}.tar.gz"
sha256 = "1e927d52e9c85d162bf985f24d13c6ccede9beb880d86fec492ed15480a5c71a"


def post_install(self):
    self.install_shell("/usr/bin/tcsh")
    self.install_license("Copyright")
