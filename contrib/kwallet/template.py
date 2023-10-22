pkgname = "kwallet"
pkgver = "6.2.1"
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
sha256 = "510c6818fb28dd91c2a90c4d05683010caf1b39e9af1b3a8cbb3b4b7c62193bc"
# FIXME: cfi kills kwalletd6 (on launch of e.g. chromium) in libKF6WalletBackend.so
hardening = ["vis", "!cfi"]


@subpackage("kwallet-devel")
def _devel(self):
    return self.default_devel()
