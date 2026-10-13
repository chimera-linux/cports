pkgname = "kitemmodels"
pkgver = "6.31.0"
pkgrel = 0
build_style = "cmake"
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = ["cmake", "extra-cmake-modules", "ninja"]
makedepends = ["qt6-qtdeclarative-devel", "qt6-qttools-devel"]
pkgdesc = "KDE's item models extending the Qt model-view framework"
license = "LGPL-2.0-only AND LGPL-2.0-or-later"
url = "https://community.kde.org/Frameworks"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kitemmodels-{pkgver}.tar.xz"
sha256 = "bcd5d95bd300c5b8b6400d087bfbf66efec34d3617aef90878e0c90407f6964c"
hardening = ["vis"]


@subpackage("kitemmodels-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
