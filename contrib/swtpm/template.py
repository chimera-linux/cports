pkgname = "swtpm"
pkgver = "0.8.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--with-gnutls",
    "--with-tss-user=tss",
    "--with-tss-group=tss",
]
make_cmd = "gmake"
hostmakedepends = [
    "automake",
    "bash",
    "expect",
    "gawk",
    "gmake",
    "gnutls-progs",
    "libtool",
    "pkgconf",
    "socat",
]
makedepends = [
    "gnutls-devel",
    "json-glib-devel",
    "libseccomp-devel",
    "libtasn1-devel",
    "libtpms-devel",
    "linux-headers",
    "openssl-devel",
]
checkdepends = [
    "iproute2",
]
depends = [
    "gnutls-progs",
    "trousers",
]
pkgdesc = "TPM emulator with socket, character device, and Linux CUSE interface"
maintainer = "cesorious <cesorious@gmail.com>"
license = "BSD-3-Clause"
url = "https://github.com/stefanberger/swtpm"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "b281b4e8c39f68e1928675f788abc70072e4081152e129144359a8c5c304c06b"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("swtpm-libs")
def _libs(self):
    return ["usr/lib/swtpm/*.so.*"]


@subpackage("swtpm-devel")
def _devel(self):
    return self.default_devel(extra=["usr/lib/swtpm/libswtpm_libtpms.a"])
