pkgname = "knotifications"
pkgver = "6.7.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
]
makedepends = [
    "kconfig-devel",
    "libcanberra-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qttools-devel",
]
pkgdesc = "KDE Desktop notifications"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "BSD-3-Clause AND LGPL-2.0-or-later AND LGPL-2.0-only AND (LGPL-2.1-only OR LGPL-3.0-only)"
url = "https://api.kde.org/frameworks/knotifications/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/knotifications-{pkgver}.tar.xz"
sha256 = "9e972f015d9b31b3283bf842a32d270096224d127c13a6e79450f4f0452de5e7"
hardening = ["vis"]


def post_install(self):
    self.install_license("LICENSES/BSD-3-Clause.txt")


@subpackage("knotifications-devel")
def _(self):
    return self.default_devel()
