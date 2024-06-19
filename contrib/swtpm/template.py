pkgname = "swtpm"
pkgver = "0.9.0"
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
checkdepends = ["iproute2"]
depends = ["gnutls-progs", "trousers"]
pkgdesc = "TPM emulator with socket, character device, and Linux CUSE interface"
maintainer = "cesorious <cesorious@gmail.com>"
license = "BSD-3-Clause"
url = "https://github.com/stefanberger/swtpm"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "9679ca171e8aaa3c4e4053e8bc1d10c8dabf0220bd4b16aba78743511c25f731"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("swtpm-libs")
def _libs(self):
    return ["usr/lib/swtpm/*.so.*"]


@subpackage("swtpm-devel")
def _devel(self):
    return self.default_devel(extra=["usr/lib/swtpm/libswtpm_libtpms.a"])
