pkgname = "libssh2"
pkgver = "1.9.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [f"--with-libssl-prefix={current.profile().sysroot / 'usr'}"]
hostmakedepends = ["pkgconf"]
makedepends = ["zlib-devel", "openssl-devel"]
pkgdesc = "Library implementing the SSH2 protocol"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://www.libssh2.org"
source = f"https://www.libssh2.org/download/{pkgname}-{pkgver}.tar.gz"
sha256 = "d5fb8bd563305fd1074dda90bd053fb2d29fc4bce048d182f96eaa466dfadafd"

def post_install(self):
    self.install_license("COPYING")

@subpackage("libssh2-devel")
def _devel(self):
    return self.default_devel(extra = ["usr/share"])
