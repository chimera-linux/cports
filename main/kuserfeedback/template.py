pkgname = "kuserfeedback"
pkgver = "6.29.0"
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
    "qt6-qttools-devel",
]
pkgdesc = "KDE user feedback integration"
license = "LGPL-2.1-or-later"
url = "https://community.kde.org/Frameworks"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kuserfeedback-{pkgver}.tar.xz"
sha256 = "36fd747bd0c8a22e3e542a4d0f05e4a85101953e19d80839a3c9cd67b5d1ac9f"
hardening = ["vis"]


@subpackage("kuserfeedback-devel")
def _(self):
    return self.default_devel()
