pkgname = "kpeople"
pkgver = "6.18.0"
pkgrel = 0
build_style = "cmake"
# FIXME: off by one in rows after merging people
make_check_args = ["-E", "personsmodeltest"]
hostmakedepends = ["cmake", "extra-cmake-modules", "gettext", "ninja"]
makedepends = [
    "kcontacts-devel",
    "kitemviews-devel",
    "kwidgetsaddons-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qttools-devel",
]
# qt sqlite use at runtime
depends = ["qt6-qtbase-sql"]
checkdepends = [*depends]
pkgdesc = "KDE contact api"
license = "LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/kpeople/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kpeople-{pkgver}.tar.xz"
sha256 = "09ba29efeb612eef4e54814f1f91e2d07c8942e6cf2c23176d9f306d68544d2b"
hardening = ["vis"]


@subpackage("kpeople-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]

    return self.default_devel()
