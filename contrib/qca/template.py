pkgname = "qca"
pkgver = "2.3.8"
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
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-or-later"
url = "https://api.kde.org/qca/html"
source = f"$(KDE_SITE)/qca/{pkgver}/qca-{pkgver}.tar.xz"
sha256 = "48759ca86a0202461d908ba66134380cc3bb7d20fed3c031b9fc0289796a8264"
hardening = ["vis", "cfi"]


@subpackage("qca-devel")
def _devel(self):
    return self.default_devel()


@subpackage("qca-progs")
def _progs(self):
    return self.default_progs()
