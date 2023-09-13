pkgname = "nftables"
pkgver = "1.0.8"
pkgrel = 1
build_style = "gnu_configure"
configure_args = [
    "--with-json",
    "--with-python-bin=/usr/bin/python3",
    "--with-cli=editline",
]
hostmakedepends = [
    "pkgconf",
    "python",
    "flex",
    "pkgconf",
    "automake",
    "libtool",
    "python-setuptools",
]
makedepends = [
    "jansson-devel",
    "libmnl-devel",
    "libnftnl-devel",
    "libedit-devel",
    "gmp-devel",
    "linux-headers",
]
pkgdesc = "Netfilter nftables userspace tools"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "http://netfilter.org/projects/nftables"
source = f"{url}/files/{pkgname}-{pkgver}.tar.xz"
sha256 = "9373740de41a82dbc98818e0a46a073faeb8a8d0689fa4fa1a74399c32bf3d50"
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


@subpackage("nftables-python")
def _py(self):
    self.pkgdesc = f"{pkgdesc} (Python bindings)"
    self.depends = [f"libnftables={pkgver}-r{pkgrel}"]

    return ["usr/lib/python3*"]
