pkgname = "kpeople"
pkgver = "6.28.0"
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
sha256 = "a5bcf11a6cbca46d4bf83399fe9c0c3c9aaf228be81b05ba966a4ba51256fd0a"
hardening = ["vis"]


@subpackage("kpeople-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]

    return self.default_devel()
