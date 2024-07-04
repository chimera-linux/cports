pkgname = "baloo-widgets"
pkgver = "24.05.2"
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
sha256 = "b7c4680fbda02f337c775e8dde91ad6f065bcdf361ce77d5422110b2b6444318"
# CFI: check
hardening = ["vis", "cfi"]
