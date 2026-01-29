# update main/python-nftables alongside this
pkgname = "nftables"
pkgver = "1.1.6"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--with-cli=editline",
    "--with-json",
]
configure_env = {
    "CONFIG_SHELL": "/usr/bin/bash",
}
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
sha256 = "372931bda8556b310636a2f9020adc710f9bab66f47efe0ce90bff800ac2530c"
hardening = ["vis", "cfi"]
# requires unshare, python, and still fails on 'nft' cmd
options = ["!check"]


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
