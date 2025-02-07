pkgname = "baloo-widgets"
pkgver = "24.12.2"
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
sha256 = "f688e4669ab30981236a2383db5787a9887f72c87536afb3105e37f588c6b5b1"
hardening = ["vis"]
