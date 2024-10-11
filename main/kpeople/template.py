pkgname = "kpeople"
pkgver = "6.7.0"
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
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/kpeople/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/kpeople-{pkgver}.tar.xz"
sha256 = "d36246bac50f5bf406f683fe61c92cb5e623a51de9ffed1104665e5f135ef888"
hardening = ["vis"]


@subpackage("kpeople-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]

    return self.default_devel()
