pkgname = "kquickcharts"
pkgver = "6.9.0"
pkgrel = 0
build_style = "cmake"
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
    "spirv-tools",
]
makedepends = [
    "qt6-qtdeclarative-devel",
]
pkgdesc = "QtQuick high-performance charts module"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/kquickcharts/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kquickcharts-{pkgver}.tar.xz"
sha256 = "df17c336aeb885e0d533916bf5211910e4f0844f8bcc8b45423dd9a0a02839ef"
hardening = ["vis"]


@subpackage("kquickcharts-devel")
def _(self):
    return self.default_devel()
