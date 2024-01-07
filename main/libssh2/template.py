pkgname = "libssh2"
pkgver = "1.11.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    f"--with-libssl-prefix={self.profile().sysroot / 'usr'}",
    "--disable-docker-tests",
]
configure_gen = []
hostmakedepends = ["pkgconf"]
makedepends = ["zlib-devel", "openssl-devel"]
checkdepends = ["bash"]
pkgdesc = "Library implementing the SSH2 protocol"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://www.libssh2.org"
source = f"https://www.libssh2.org/download/{pkgname}-{pkgver}.tar.gz"
sha256 = "3736161e41e2693324deb38c26cfdc3efe6209d634ba4258db1cecff6a5ad461"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libssh2-devel")
def _devel(self):
    return self.default_devel()
