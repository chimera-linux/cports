pkgname = "baloo-widgets"
pkgver = "24.12.0"
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
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only)"
url = "https://api.kde.org/baloo-widgets/html/index.html"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/baloo-widgets-{pkgver}.tar.xz"
)
sha256 = "98893290528c2d82d851c5c743e64a4b7d44a3805cd38a33b0c5e462e3eeb616"
hardening = ["vis"]
