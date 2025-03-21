pkgname = "kpeople"
pkgver = "6.12.0"
pkgrel = 0
build_style = "cmake"
# FIXME: off by one in rows after merging people
make_check_args = ["-E", "personsmodeltest"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
]
makedepends = [
    "kcontacts-devel",
    "kitemviews-devel",
    "kwidgetsaddons-devel",
    "qt6-qtdeclarative-devel",
]
# qt sqlite use at runtime
depends = ["qt6-qtbase-sql"]
checkdepends = [*depends]
pkgdesc = "KDE contact api"
license = "LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/kpeople/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kpeople-{pkgver}.tar.xz"
sha256 = "a43ddde783250d7fb59d3dfcd780cf27ab7e4028f6b27c03551fd17a2d3157e6"
hardening = ["vis"]


@subpackage("kpeople-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]

    return self.default_devel()
