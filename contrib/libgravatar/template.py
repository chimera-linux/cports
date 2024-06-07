pkgname = "libgravatar"
pkgver = "24.05.0"
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
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.0-or-later"
url = "https://api.kde.org/kdepim/libgravatar/html"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/libgravatar-{pkgver}.tar.xz"
sha256 = "53c459927a00b4504a03684a6f06b0f801c66f31b0f7202ce64d7d905977f4fb"


@subpackage("libgravatar-devel")
def _devel(self):
    return self.default_devel()
