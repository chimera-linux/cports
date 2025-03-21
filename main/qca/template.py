pkgname = "qca"
pkgver = "2.3.10"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_WITH_QT6=ON"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    "libgcrypt-devel",
    "libsasl-devel",
    "pkcs11-helper-devel",
    "qt6-qt5compat-devel",
]
pkgdesc = "Qt6 cryptographic architecture"
license = "LGPL-2.1-or-later"
url = "https://api.kde.org/qca/html"
source = f"$(KDE_SITE)/qca/{pkgver}/qca-{pkgver}.tar.xz"
sha256 = "1c5b722da93d559365719226bb121c726ec3c0dc4c67dea34f1e50e4e0d14a02"
hardening = ["vis"]


@subpackage("qca-devel")
def _(self):
    return self.default_devel()


@subpackage("qca-progs")
def _(self):
    return self.default_progs()
