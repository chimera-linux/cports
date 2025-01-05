pkgname = "tcsh"
pkgver = "6.24.14"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-nls"]
hostmakedepends = ["automake"]
makedepends = ["ncurses-devel"]
pkgdesc = "Enhanced version of the Berkeley UNIX C shell"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://astron.com/pub/tcsh"
source = f"{url}/tcsh-{pkgver}.tar.gz"
sha256 = "36880f258a63fc11fe72a65098b585ebc4ecdee24388b8ebec97e6ae8e485318"


def post_install(self):
    self.install_shell("/usr/bin/tcsh")
    self.install_license("Copyright")
