pkgname = "rpcbind"
pkgver = "1.2.6"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-warmstarts",
    "--with-rpcuser=_rpc",
    "--with-statedir=/var/lib/rpcbind",
    "--with-systemdsystemunitdir=no",
]
hostmakedepends = ["automake", "pkgconf"]
makedepends = ["libtirpc-devel", "musl-bsd-headers"]
pkgdesc = "Universal addresses to RPC program number mapper"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://linux-nfs.org"
source = f"https://sourceforge.net/projects/rpcbind/files/rpcbind/{pkgver}/rpcbind-{pkgver}.tar.bz2"
sha256 = "5613746489cae5ae23a443bb85c05a11741a5f12c8f55d2bb5e83b9defeee8de"
hardening = ["!cfi", "vis"]
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("COPYING")
    self.install_service(self.files_path / "rpcbind")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
