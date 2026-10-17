pkgname = "qca"
pkgver = "2.3.12"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_WITH_QT6=ON"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    "libgcrypt-devel",
    "libsasl-devel",
    "openssl3-devel",
    "pkcs11-helper-devel",
    "qt6-qt5compat-devel",
]
pkgdesc = "Qt6 cryptographic architecture"
license = "LGPL-2.1-or-later"
url = "https://invent.kde.org/libraries/qca"
source = f"$(KDE_SITE)/qca/{pkgver}/qca-{pkgver}.tar.xz"
sha256 = "d4a2b3aa0272d73ea0c4cd2140960177fa34ddc2030e59a48ecfb80c757572c3"
hardening = ["vis"]


@subpackage("qca-devel")
def _(self):
    return self.default_devel()


@subpackage("qca-progs")
def _(self):
    return self.default_progs()
