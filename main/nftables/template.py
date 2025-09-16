# update main/python-nftables alongside this
pkgname = "nftables"
pkgver = "1.1.3"
pkgrel = 0
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
    "dinit-chimera",
    "gmp-devel",
    "jansson-devel",
    "libedit-devel",
    "libmnl-devel",
    "libnftnl-devel",
    "linux-headers",
]
pkgdesc = "Netfilter nftables userspace tools"
license = "GPL-2.0-only AND GPL-2.0-or-later"
url = "http://netfilter.org/projects/nftables"
source = f"{url}/files/nftables-{pkgver}.tar.xz"
sha256 = "9c8a64b59c90b0825e540a9b8fcb9d2d942c636f81ba50199f068fde44f34ed8"
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
