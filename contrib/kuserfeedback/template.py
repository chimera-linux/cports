pkgname = "kuserfeedback"
pkgver = "6.3.0"
pkgrel = 0
build_style = "cmake"
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "bison",
    "cmake",
    "extra-cmake-modules",
    "flex",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "qt6-qtdeclarative-devel",
    "qt6-qtcharts-devel",
    "qt6-qtsvg-devel",
    "qt6-qttools-devel",
]
checkdepends = ["xwayland-run"]
pkgdesc = "KDE user feedback integration"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/kuserfeedback/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/kuserfeedback-{pkgver}.tar.xz"
sha256 = "3fe2ce37b92a70d604f38fa369b5fe2ea64e268c48aa450e9971fc8404e87006"
# FIXME: cfi makes openglinfosourcetest fail
hardening = ["vis", "!cfi"]


@subpackage("kuserfeedback-devel")
def _devel(self):
    return self.default_devel()
