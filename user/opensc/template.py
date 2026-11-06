pkgname = "opensc"
pkgver = "0.27.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-static",
    "--disable-integration-tests",  # needs softhsm
    "--enable-p11_system_config_modules=/usr/share/p11-kit/modules",
    "--with-completiondir=/usr/share/bash-completion/completions",
    "--with-xsl-stylesheetsdir=/usr/share/xsl/docbook",
]
hostmakedepends = [
    "automake",
    "docbook-xsl",
    "libxslt-progs",
    "pkgconf",
    "slibtool",
]
makedepends = [
    "bash-completion",
    "cmocka-devel",
    "glib-devel",
    "openssl3-devel",
    "p11-kit-devel",
    "pcsc-lite-devel",
    "readline-devel",
    "zlib-ng-compat-devel",
]
# dlopens libpcsclite.so.1
depends = ["pcsc-lite"]
pkgdesc = "Tools and libraries for smart cards"
license = "LGPL-2.1-or-later"
url = "https://github.com/OpenSC/OpenSC"
source = f"{url}/releases/download/{pkgver}/opensc-{pkgver}.tar.gz"
sha256 = "976f4a23eaf3397a1a2c3a7aac80bf971a8c3d829c9a79f06145bfaeeae5eca7"


def post_install(self):
    # empty stub, the annotated example is already in docs
    self.uninstall("etc/opensc.conf")
    # npa-tool is only built with openpace
    self.uninstall("usr/share/bash-completion/completions/npa-tool")


@subpackage("opensc-devel")
def _(self):
    # onepin-opensc-pkcs11.so and libsmm-local.so
    # symlinks are loaded at runtime by these names
    return ["usr/lib/libopensc.so", "usr/lib/pkgconfig"]
