pkgname = "plasma-disks"
pkgver = "6.4.5"
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
    "kauth-devel",
    "kcmutils-devel",
    "kcoreaddons-devel",
    "kdbusaddons-devel",
    "ki18n-devel",
    "kio-devel",
    "knotifications-devel",
    "kservice-devel",
    "qt6-qtdeclarative-devel",
    "solid-devel",
]
depends = ["smartmontools"]
checkdepends = ["xwayland-run"]
pkgdesc = "KDE disk failure monitor"
license = "GPL-2.0-only OR GPL-3.0-only"
url = "https://invent.kde.org/plasma/plasma-disks"
source = f"$(KDE_SITE)/plasma/{pkgver}/plasma-disks-{pkgver}.tar.xz"
sha256 = "8017c749fbc850a13d11d5b35343f85194ad4276a01cc05311dd69828f51fef3"
hardening = ["vis"]
