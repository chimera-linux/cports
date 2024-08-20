pkgname = "qca"
pkgver = "2.3.9"
pkgrel = 1
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
sha256 = "c555d5298cdd7b6bafe2b1f96106f30cfa543a23d459d50c8a91eac33c476e4e"
hardening = ["vis"]


@subpackage("qca-devel")
def _(self):
    return self.default_devel()


@subpackage("qca-progs")
def _(self):
    return self.default_progs()
