pkgname = "swtpm"
pkgver = "0.10.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--libexecdir=/usr/lib",  # XXX drop libexec
    "--with-gnutls",
    "--with-tss-user=tss",
    "--with-tss-group=tss",
]
# test compat
make_dir = "."
hostmakedepends = [
    "automake",
    "bash",
    "gawk",
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
    "openssl3-devel",
]
checkdepends = ["iproute2"]
depends = ["gnutls-progs", "trousers"]
pkgdesc = "TPM emulator with socket, character device, and Linux CUSE interface"
license = "BSD-3-Clause"
url = "https://github.com/stefanberger/swtpm"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "f8da11cadfed27e26d26c5f58a7b8f2d14d684e691927348906b5891f525c684"


def post_install(self):
    self.install_license("LICENSE")
    self.install_tmpfiles("^/tmpfiles.conf")
    self.uninstall("usr/lib/installed-tests")


@subpackage("swtpm-libs")
def _(self):
    return ["usr/lib/swtpm/*.so.*"]


@subpackage("swtpm-devel")
def _(self):
    return self.default_devel(extra=["usr/lib/swtpm/libswtpm_libtpms.a"])
