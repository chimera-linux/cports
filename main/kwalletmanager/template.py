pkgname = "kwalletmanager"
pkgver = "24.12.2"
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
    "karchive-devel",
    "kauth-devel",
    "kcmutils-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "kdoctools-devel",
    "ki18n-devel",
    "kio-devel",
    "kservice-devel",
    "kstatusnotifieritem-devel",
    "kwallet-devel",
    "kwindowsystem-devel",
    "kxmlgui-devel",
    "qt6-qtdeclarative-devel",
]
pkgdesc = "KDE KWallet GUI manager"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://invent.kde.org/utilities/kwalletmanager"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/kwalletmanager-{pkgver}.tar.xz"
)
sha256 = "68fc74803068cfbb84ce98a5a25fe4989eef96b42418803ad2245bc51f060627"
hardening = ["vis"]
