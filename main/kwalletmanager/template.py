pkgname = "kwalletmanager"
pkgver = "25.08.0"
pkgrel = 0
build_style = "cmake"
# XXX drop libexec
configure_args = ["-DCMAKE_INSTALL_LIBEXECDIR=/usr/lib"]
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
license = "GPL-2.0-or-later"
url = "https://invent.kde.org/utilities/kwalletmanager"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/kwalletmanager-{pkgver}.tar.xz"
)
sha256 = "0110bbc55733392f49d2de333082d29c1929a1073af27799f6c277289c8359a3"
hardening = ["vis"]
