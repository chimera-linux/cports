pkgname = "kwallet"
pkgver = "6.3.0"
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
sha256 = "edb6ebbfa3d90869cadfc9266da47a8b3d5b2b5b0e496b74a7ea5262392d2add"
# FIXME: cfi kills kwalletd6 (on launch of e.g. chromium) in libKF6WalletBackend.so
hardening = ["vis", "!cfi"]


@subpackage("kwallet-devel")
def _devel(self):
    return self.default_devel()
