pkgname = "libssh2"
pkgver = "1.10.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [f"--with-libssl-prefix={self.profile().sysroot / 'usr'}"]
hostmakedepends = ["pkgconf"]
makedepends = ["zlib-devel", "openssl-devel"]
pkgdesc = "Library implementing the SSH2 protocol"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://www.libssh2.org"
source = f"https://www.libssh2.org/download/{pkgname}-{pkgver}.tar.gz"
sha256 = "2d64e90f3ded394b91d3a2e774ca203a4179f69aebee03003e5a6fa621e41d51"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libssh2-devel")
def _devel(self):
    return self.default_devel()


configure_gen = []
