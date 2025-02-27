pkgname = "tcsh"
pkgver = "6.24.15"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-nls"]
hostmakedepends = ["automake"]
makedepends = ["ncurses-devel"]
pkgdesc = "Enhanced version of the Berkeley UNIX C shell"
license = "BSD-2-Clause"
url = "https://astron.com/pub/tcsh"
source = f"{url}/tcsh-{pkgver}.tar.gz"
sha256 = "d4d0b2a4df320f57a518e44c359ef36bbcf85d64f5146d0cb8ff34984e0d23fd"


def post_install(self):
    self.install_shell("/usr/bin/tcsh")
    self.install_license("Copyright")
