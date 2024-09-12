pkgname = "kwalletmanager"
pkgver = "24.08.1"
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
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-2.0-or-later"
url = "https://invent.kde.org/utilities/kwalletmanager"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/kwalletmanager-{pkgver}.tar.xz"
)
sha256 = "d006b9bb3d4e0a3c77d2a73fbfe150f37b3c2a3fe526442031accf1dc1bb3aa5"
hardening = ["vis"]
