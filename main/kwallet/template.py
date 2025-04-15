pkgname = "kwallet"
pkgver = "6.13.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
]
makedepends = [
    "gpgme-devel",
    "kcolorscheme-devel",
    "kconfig-devel",
    "kcoreaddons-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "kdoctools-devel",
    "ki18n-devel",
    "knotifications-devel",
    "kservice-devel",
    "kwidgetsaddons-devel",
    "kwindowsystem-devel",
    "libgcrypt-devel",
    "qca-devel",
    "qt6-qtdeclarative-devel",
]
pkgdesc = "KDE Safe desktop-wide storage for passwords"
license = "LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/kwallet/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kwallet-{pkgver}.tar.xz"
sha256 = "1a6ff2ccf660a433bda6b00ac873796dcb46bd2443787fcf5fbe4c433ca8cb36"
hardening = ["vis"]


@subpackage("kwallet-devel")
def _(self):
    return self.default_devel()
