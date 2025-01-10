pkgname = "kitemmodels"
pkgver = "6.10.0"
pkgrel = 0
build_style = "cmake"
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
]
makedepends = [
    "qt6-qtdeclarative-devel",
]
pkgdesc = "KDE's item models extending the Qt model-view framework"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.0-only AND LGPL-2.0-or-later"
url = "https://api.kde.org/frameworks/kitemmodels/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kitemmodels-{pkgver}.tar.xz"
sha256 = "83859a4aee67bf5e768a93325422264cb9e847013f281c5cb02e631c3b3b0007"
hardening = ["vis"]


@subpackage("kitemmodels-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
