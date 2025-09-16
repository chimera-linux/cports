pkgname = "rpcbind"
pkgver = "1.2.7"
pkgrel = 1
build_style = "gnu_configure"
configure_args = [
    "--enable-warmstarts",
    "--with-rpcuser=_rpc",
    "--with-statedir=/var/lib/rpcbind",
    "--with-systemdsystemunitdir=no",
]
hostmakedepends = ["automake", "pkgconf"]
makedepends = ["dinit-chimera", "libtirpc-devel", "musl-bsd-headers"]
pkgdesc = "Universal addresses to RPC program number mapper"
license = "BSD-3-Clause"
url = "https://linux-nfs.org"
source = f"https://sourceforge.net/projects/rpcbind/files/rpcbind/{pkgver}/rpcbind-{pkgver}.tar.bz2"
sha256 = "f6edf8cdf562aedd5d53b8bf93962d61623292bfc4d47eedd3f427d84d06f37e"
hardening = ["!cfi", "vis"]
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("COPYING")
    self.install_service(self.files_path / "rpcbind")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
