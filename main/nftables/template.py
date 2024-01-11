# update main/python-nftables alongside this
pkgname = "nftables"
pkgver = "1.0.9"
pkgrel = 1
build_style = "gnu_configure"
configure_args = [
    "--with-cli=editline",
    "--with-json",
]
hostmakedepends = [
    "automake",
    "flex",
    "libtool",
    "pkgconf",
]
makedepends = [
    "gmp-devel",
    "jansson-devel",
    "libedit-devel",
    "libmnl-devel",
    "libnftnl-devel",
    "linux-headers",
]
pkgdesc = "Netfilter nftables userspace tools"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only AND GPL-2.0-or-later"
url = "http://netfilter.org/projects/nftables"
source = f"{url}/files/{pkgname}-{pkgver}.tar.xz"
sha256 = "a3c304cd9ba061239ee0474f9afb938a9bb99d89b960246f66f0c3a0a85e14cd"
hardening = ["vis", "cfi"]


def post_install(self):
    fpath = self.files_path
    self.install_file(fpath / "nftables-start", "usr/libexec", mode=0o755)
    self.install_service(fpath / "nftables")


@subpackage("libnftables")
def _lib(self):
    self.pkgdesc = f"{pkgdesc} (runtime library)"

    return self.default_libs()


@subpackage("nftables-devel")
def _devel(self):
    return self.default_devel()
