# update main/python-nftables alongside this
pkgname = "nftables"
pkgver = "1.1.7"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--with-cli=editline",
    "--with-json",
]
configure_env = {"CONFIG_SHELL": "/usr/bin/bash"}
hostmakedepends = [
    "automake",
    "bash",
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
sha256 = "a6fbf060d8d4fff001517a2b94f356bb4366bfbf0ba366366f9d27cc38caa58f"
hardening = ["vis", "cfi"]
# requires a bunch of stuff we can't provide here
options = ["etcfiles", "!check"]


def post_install(self):
    fpath = self.files_path
    self.install_file(fpath / "nftables-start", "usr/lib", mode=0o755)
    self.install_service(fpath / "nftables")


@subpackage("nftables-libs")
def _(self):
    # transitional
    self.provides = [self.with_pkgver("libnftables")]

    return self.default_libs()


@subpackage("nftables-devel")
def _(self):
    return self.default_devel()
