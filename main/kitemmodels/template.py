pkgname = "kitemmodels"
pkgver = "6.15.0"
pkgrel = 0
build_style = "cmake"
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = ["cmake", "extra-cmake-modules", "ninja"]
makedepends = ["qt6-qtdeclarative-devel", "qt6-qttools-devel"]
pkgdesc = "KDE's item models extending the Qt model-view framework"
license = "LGPL-2.0-only AND LGPL-2.0-or-later"
url = "https://api.kde.org/frameworks/kitemmodels/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kitemmodels-{pkgver}.tar.xz"
sha256 = "8e8c9d31a00c41ed836189755a86b82fd968474d6388f033259dd65ab18e7c94"
hardening = ["vis"]


@subpackage("kitemmodels-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
