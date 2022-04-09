pkgname = "nftables"
pkgver = "1.0.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--with-json", "--with-python-bin=/usr/bin/python3", "--with-cli=editline"
]
hostmakedepends = ["pkgconf", "python", "flex", "pkgconf"]
makedepends = [
    "jansson-devel", "libmnl-devel", "libnftnl-devel", "libedit-devel",
    "gmp-devel", "linux-headers"
]
pkgdesc = "Netfilter nftables userspace tools"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "http://netfilter.org/projects/nftables"
source = f"{url}/files/{pkgname}-{pkgver}.tar.bz2"
sha256 = "0b28a36ffcf4567b841de7bd3f37918b1fed27859eb48bdec51e1f7a83954c02"

def post_install(self):
    self.install_service(self.files_path / "nftables")

@subpackage("libnftables")
def _lib(self):
    self.pkgdesc = f"{pkgdesc} (runtime library)"

    return self.default_libs()

@subpackage("nftables-devel")
def _devel(self):
    return self.default_devel()
