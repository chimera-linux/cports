pkgname = "plasma-firewall"
pkgver = "6.7.91"
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
source = f"$(KDE_UNSTABLE_SITE)/plasma/{pkgver}/plasma-firewall-{pkgver}.tar.xz"
sha256 = "02ea4b1982c679a78ef603a73bebe2ce1120dd97bfa6f02bcf69cc8f26d3eff6"
