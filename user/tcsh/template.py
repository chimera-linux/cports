pkgname = "tcsh"
pkgver = "6.24.16"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-nls"]
hostmakedepends = ["automake"]
makedepends = ["ncurses-devel"]
pkgdesc = "Enhanced version of the Berkeley UNIX C shell"
license = "BSD-2-Clause"
url = "https://astron.com/pub/tcsh"
source = f"{url}/tcsh-{pkgver}.tar.gz"
sha256 = "4208cf4630fb64d91d81987f854f9570a5a0e8a001a92827def37d0ed8f37364"


def post_install(self):
    self.install_shell("/usr/bin/tcsh")
    self.install_license("Copyright")
