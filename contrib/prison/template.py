pkgname = "prison"
pkgver = "6.3.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
]
makedepends = [
    "libdmtx-devel",
    "qrencode-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtmultimedia-devel",
    "zxing-cpp-devel",
]
pkgdesc = "KDE library to produce QR codes and DataMatrix barcodes"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "MIT"
url = "https://api.kde.org/frameworks/prison/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/prison-{pkgver}.tar.xz"
sha256 = "769807725787051e5e9a2f41eb7f791a9ce11be775a7eeff8d525f2a78b4bc46"
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("LICENSES/MIT.txt")


@subpackage("prison-devel")
def _devel(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
