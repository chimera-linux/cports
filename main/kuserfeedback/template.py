pkgname = "kuserfeedback"
pkgver = "6.7.0"
pkgrel = 0
build_style = "cmake"
# fails without gl
make_check_args = ["-E", "openglinfosourcetest"]
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
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
pkgdesc = "KDE user feedback integration"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/kuserfeedback/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/kuserfeedback-{pkgver}.tar.xz"
sha256 = "4def8d0d6ef227807b6066cb762cec352452a18e0e28b56aecce8ef3ceb52761"
hardening = ["vis"]


@subpackage("kuserfeedback-devel")
def _(self):
    return self.default_devel()
