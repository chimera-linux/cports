pkgname = "baloo-widgets"
pkgver = "25.04.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DQT_MAJOR_VERSION=6"]
# FIXME: 'not connected to dbus server'
make_check_args = ["-E", "filemetadataitemcounttest"]
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "baloo-devel",
    "kconfig-devel",
    "kio-devel",
    "ki18n-devel",
    "kservice-devel",
]
checkdepends = ["xwayland-run"]
pkgdesc = "KDE Baloo widgets"
license = "LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only)"
url = "https://api.kde.org/baloo-widgets/html/index.html"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/baloo-widgets-{pkgver}.tar.xz"
)
sha256 = "a3dc18ddd6059c88a113da09a5472a93cf08f11dd0c358c3d3b6a98127c45c45"
hardening = ["vis"]
