# update main/python-nftables alongside this
pkgname = "nftables"
pkgver = "1.1.1"
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
source = f"{url}/files/nftables-{pkgver}.tar.xz"
sha256 = "6358830f3a64f31e39b0ad421d7dadcd240b72343ded48d8ef13b8faf204865a"
hardening = ["vis", "cfi"]


def post_install(self):
    fpath = self.files_path
    self.install_file(fpath / "nftables-start", "usr/libexec", mode=0o755)
    self.install_service(fpath / "nftables")


@subpackage("nftables-libs")
def _(self):
    # transitional
    self.provides = [self.with_pkgver("libnftables")]

    return self.default_libs()


@subpackage("nftables-devel")
def _(self):
    return self.default_devel()
