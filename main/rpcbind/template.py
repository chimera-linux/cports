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
hostmakedepends = [
    "automake",
    "pkgconf",
]
makedepends = ["libtirpc-devel", "musl-bsd-headers"]
pkgdesc = "Universal addresses to RPC program number mapper"
maintainer = "miko <mikoxyzzz@gmail.com>"
license = "BSD-3-Clause"
url = "https://linux-nfs.org"
source = f"https://sourceforge.net/projects/rpcbind/files/rpcbind/{pkgver}/rpcbind-{pkgver}.tar.bz2"
sha256 = "5613746489cae5ae23a443bb85c05a11741a5f12c8f55d2bb5e83b9defeee8de"
# FIXME: cfi
hardening = ["!cfi", "vis"]
# no tests
options = ["!check"]


def post_install(self):
    for n in ["sysusers", "tmpfiles"]:
        self.install_file(
            self.files_path / f"{n}.conf",
            f"usr/lib/{n}.d",
            name="rpcbind.conf",
        )

    self.install_license("COPYING")
    self.install_service(self.files_path / "rpcbind")
