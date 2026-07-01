pkgname = "plasma-firewall"
pkgver = "6.7.2"
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
    "kauth-devel",
    "kcmutils-devel",
    "kconfig-devel",
    "ki18n-devel",
    "libplasma-devel",
    "qt6-qtdeclarative-devel",
]
checkdepends = ["xwayland-run"]
pkgdesc = "KDE control panel for the system firewall"
license = "GPL-3.0-only"
url = "https://invent.kde.org/plasma/plasma-firewall"
source = f"$(KDE_SITE)/plasma/{pkgver}/plasma-firewall-{pkgver}.tar.xz"
sha256 = "4cf3c1ac4f1f08e23604f49d61bb61fc1e04bb8295680680b6d74257c3278bca"
