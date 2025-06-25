pkgname = "plasma-disks"
pkgver = "6.4.1"
pkgrel = 0
build_style = "cmake"
# XXX drop libexec
configure_args = ["-DCMAKE_INSTALL_LIBEXECDIR=/usr/lib"]
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kcoreaddons-devel",
    "kdbusaddons-devel",
    "knotifications-devel",
    "ki18n-devel",
    "solid-devel",
    "kservice-devel",
    "kio-devel",
    "kauth-devel",
    "kcmutils-devel",
    "qt6-qtdeclarative-devel",
]
depends = ["smartmontools"]
checkdepends = ["xwayland-run"]
pkgdesc = "KDE disk failure monitor"
license = "GPL-2.0-only OR GPL-3.0-only"
url = "https://invent.kde.org/plasma/plasma-disks"
source = f"$(KDE_SITE)/plasma/{pkgver}/plasma-disks-{pkgver}.tar.xz"
sha256 = "c98f9a0d5322982a908497d7cc02867825486257b8e25462d197f336011c5314"
hardening = ["vis"]
