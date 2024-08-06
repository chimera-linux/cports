pkgname = "plasma-disks"
pkgver = "6.1.4"
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
sha256 = "795f6bdaba2fe979d5836479111fc3d6fc6b2a0b355b48c8333db5abb5df4c47"
hardening = ["vis"]
