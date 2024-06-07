pkgname = "kbookmarks"
pkgver = "6.3.0"
pkgrel = 0
build_style = "cmake"
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
]
makedepends = [
    "kconfig-devel",
    "kconfigwidgets-devel",
    "kcoreaddons-devel",
    "kwidgetsaddons-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qttools-devel",
]
pkgdesc = "KDE Bookmarks management library"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/kbookmarks/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/kbookmarks-{pkgver}.tar.xz"
sha256 = "f0789daaab86b0c2451a91e21327f20bf1d200491cf7744af93c262aa76cfea1"
hardening = ["vis", "!cfi"]


@subpackage("kbookmarks-devel")
def _devel(self):
    self.depends += ["kwidgetsaddons-devel"]

    return self.default_devel()
