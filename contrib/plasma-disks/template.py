pkgname = "plasma-disks"
pkgver = "6.1.5"
pkgrel = 0
build_style = "cmake"
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
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-only OR GPL-3.0-only"
url = "https://invent.kde.org/plasma/plasma-disks"
source = f"$(KDE_SITE)/plasma/{pkgver}/plasma-disks-{pkgver}.tar.xz"
sha256 = "5d7669c019e8be668b985d73d7f0fdb315984a90ac7b0cf1e3989b80946e6c4a"
hardening = ["vis"]
