pkgname = "libgravatar"
pkgver = "25.12.0"
pkgrel = 0
build_style = "cmake"
# needs net
make_check_args = ["-E", "gravatarresolvurljobtest"]
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kconfig-devel",
    "ki18n-devel",
    "kio-devel",
    "ktextwidgets-devel",
    "kwidgetsaddons-devel",
    "pimcommon-devel",
    "qt6-qtdeclarative-devel",
]
checkdepends = ["xwayland-run"]
pkgdesc = "KDE PIM Gravatar lookup library"
license = "LGPL-2.0-or-later"
url = "https://api.kde.org/kdepim/libgravatar/html"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/libgravatar-{pkgver}.tar.xz"
sha256 = "e44b573a3de25cc59cc7e147e8579939aef72c457be2e3e4ad4c16d3d9f4af7e"


@subpackage("libgravatar-devel")
def _(self):
    return self.default_devel()
