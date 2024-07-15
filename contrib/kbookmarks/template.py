pkgname = "kbookmarks"
pkgver = "6.4.0"
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
sha256 = "13c72b0c47e333ada60a4665af7829910f5c83dd6ed57789fa3229ca68ad3280"
hardening = ["vis"]


@subpackage("kbookmarks-devel")
def _devel(self):
    self.depends += ["kwidgetsaddons-devel"]

    return self.default_devel()
