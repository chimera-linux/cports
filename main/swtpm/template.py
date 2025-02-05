pkgname = "swtpm"
pkgver = "0.10.0"
pkgrel = 2
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
maintainer = "cesorious <cesorious@gmail.com>"
license = "BSD-3-Clause"
url = "https://github.com/stefanberger/swtpm"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "9f10ae0d3123ab05c3808f8c8d39f633cf1a0cf142d6ac9b87b8364a682ac842"


def post_install(self):
    self.install_license("LICENSE")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.uninstall("usr/lib/installed-tests")


@subpackage("swtpm-libs")
def _(self):
    return ["usr/lib/swtpm/*.so.*"]


@subpackage("swtpm-devel")
def _(self):
    return self.default_devel(extra=["usr/lib/swtpm/libswtpm_libtpms.a"])
