pkgname = "plasma-firewall"
pkgver = "6.5.4"
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
sha256 = "2c3fe4e4eff31b6bf069485fe58da47ea9d92c35db53cf049a5e095042442210"
