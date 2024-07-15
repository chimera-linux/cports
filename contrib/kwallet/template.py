pkgname = "kwallet"
pkgver = "6.4.0"
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
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/kwallet/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/kwallet-{pkgver}.tar.xz"
sha256 = "b2885a088e5f70754511cc1ddb0a434c1a6d7939d9c77ffc36e95483491f9e40"
hardening = ["vis"]


@subpackage("kwallet-devel")
def _devel(self):
    return self.default_devel()
