pkgname = "libgravatar"
pkgver = "26.08.1"
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
url = "https://community.kde.org/KDE_PIM"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/libgravatar-{pkgver}.tar.xz"
sha256 = "459e245db0872ee5f780d4cc90808e90d9fcb63f0ee9c22552c15d60754c388f"


@subpackage("libgravatar-devel")
def _(self):
    return self.default_devel()
