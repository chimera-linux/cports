pkgname = "libgravatar"
pkgver = "25.04.0"
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
sha256 = "6229494e60ef2fad87eb54d461d9d38b4708e6fd8749f1b6192911d12ad87bfa"


@subpackage("libgravatar-devel")
def _(self):
    return self.default_devel()
