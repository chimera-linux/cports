pkgname = "kpeople"
pkgver = "6.3.0"
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
checkdepends = list(depends)
pkgdesc = "KDE contact api"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/kpeople/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/kpeople-{pkgver}.tar.xz"
sha256 = "967f979e56acdf546198c1950e554663c963aeec56e20405607878294772303e"
hardening = ["vis", "!cfi"]


@subpackage("kpeople-devel")
def _devel(self):
    self.depends += ["qt6-qtbase-devel"]

    return self.default_devel()
