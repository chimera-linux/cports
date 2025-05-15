pkgname = "kwallet"
pkgver = "6.14.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
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
    "libsecret-devel",
    "qca-devel",
    "qt6-qtdeclarative-devel",
]
pkgdesc = "KDE Safe desktop-wide storage for passwords"
license = "LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/kwallet/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kwallet-{pkgver}.tar.xz"
sha256 = "a7477e4e5e7ccb43491c5a0eccadf6a33e962088d5af32c4b6b4aacb920f59e3"
hardening = ["vis"]


@subpackage("kwallet-devel")
def _(self):
    return self.default_devel()
