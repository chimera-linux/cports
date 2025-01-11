pkgname = "libgravatar"
pkgver = "24.12.1"
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
sha256 = "c65c615f4492c7c5b10edc66e9cfa2866daeaa7f4f1db26b583440da6d133abf"


@subpackage("libgravatar-devel")
def _(self):
    return self.default_devel()
