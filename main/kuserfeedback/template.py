pkgname = "kuserfeedback"
pkgver = "6.11.0"
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
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kuserfeedback-{pkgver}.tar.xz"
sha256 = "ac516b7b8f9cd0891664f8b580d0a5a5c494cf6b5dbfddd87b6f6256548b7910"
hardening = ["vis"]


@subpackage("kuserfeedback-devel")
def _(self):
    return self.default_devel()
