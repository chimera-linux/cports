pkgname = "prison"
pkgver = "6.31.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "extra-cmake-modules", "ninja"]
makedepends = [
    "libdmtx-devel",
    "qrencode-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtmultimedia-devel",
    "qt6-qttools-devel",
    "zxing-cpp-devel",
]
pkgdesc = "KDE library to produce QR codes and DataMatrix barcodes"
license = "MIT"
url = "https://community.kde.org/Frameworks"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/prison-{pkgver}.tar.xz"
sha256 = "30cdb5564ef76c4c2a6fe509234095c1329f30165243b81008312a1182d326bc"
hardening = ["vis"]


def post_install(self):
    self.install_license("LICENSES/MIT.txt")


@subpackage("prison-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
