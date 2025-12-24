pkgname = "opensc"
pkgver = "0.26.1"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "bash-completion",
    "pkgconf",
    "slibtool",
]
makedepends = [
    "glib-devel",
    # see post_install
    # "openpace-devel",
    "openssl3-devel",
    "pcsc-lite-devel",
    "readline-devel",
    "zlib-ng-devel",
]
checkdepends = [
    "cmocka-devel",
]
pkgdesc = "Smart card tools and middleware"
license = "LGPL-2.1-or-later"
url = "https://github.com/OpenSC/OpenSC"
source = f"{url}/releases/download/{pkgver}/opensc-{pkgver}.tar.gz"
sha256 = "f16291a031d86e570394762e9f35eaf2fcbc2337a49910f3feae42d54e1688cb"


def post_install(self):
    # NOTE: remove if OpenPACE is packaged and added to makedepends
    self.uninstall("usr/share/bash-completion/completions/npa-tool")


@subpackage("opensc-devel")
def _(self):
    # exclude symlinks to non-library shared objects (onepin-opensc-pkcs11.so@ -> opensc-pkcs11.so)
    return [
        "usr/lib/*.a",
        "usr/lib/lib*.so",
        "usr/lib/pkgconfig",
    ]
