pkgname = "libgravatar"
pkgver = "25.04.2"
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
    "ki18n-devel",
    "kconfig-devel",
    "kwidgetsaddons-devel",
    "ktextwidgets-devel",
    "kio-devel",
    "pimcommon-devel",
    "qt6-qtdeclarative-devel",
]
checkdepends = ["xwayland-run"]
pkgdesc = "KDE PIM Gravatar lookup library"
license = "LGPL-2.0-or-later"
url = "https://api.kde.org/kdepim/libgravatar/html"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/libgravatar-{pkgver}.tar.xz"
sha256 = "40ccbcd2af7ff3963bd55d5ebbc2608b1a2920ffc2e4a8aa7e97e504ae1a00f0"


@subpackage("libgravatar-devel")
def _(self):
    return self.default_devel()
