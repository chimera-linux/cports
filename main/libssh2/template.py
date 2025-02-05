pkgname = "libssh2"
pkgver = "1.11.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    f"--with-libssl-prefix={self.profile().sysroot / 'usr'}",
    "--disable-docker-tests",
]
configure_gen = []
hostmakedepends = ["pkgconf"]
makedepends = ["zlib-ng-compat-devel", "openssl3-devel"]
checkdepends = ["bash"]
pkgdesc = "Library implementing the SSH2 protocol"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://www.libssh2.org"
source = f"https://www.libssh2.org/download/libssh2-{pkgver}.tar.gz"
sha256 = "d9ec76cbe34db98eec3539fe2c899d26b0c837cb3eb466a56b0f109cabf658f7"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libssh2-devel")
def _(self):
    return self.default_devel()
