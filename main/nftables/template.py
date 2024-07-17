# update main/python-nftables alongside this
pkgname = "nftables"
pkgver = "1.1.0"
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
sha256 = "ef3373294886c5b607ee7be82c56a25bc04e75f802f8e8adcd55aac91eb0aa24"
hardening = ["vis", "cfi"]


def post_install(self):
    fpath = self.files_path
    self.install_file(fpath / "nftables-start", "usr/libexec", mode=0o755)
    self.install_service(fpath / "nftables")


@subpackage("libnftables")
def _lib(self):
    self.subdesc = "runtime library"

    return self.default_libs()


@subpackage("nftables-devel")
def _devel(self):
    return self.default_devel()
