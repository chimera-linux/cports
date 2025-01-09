pkgname = "prison"
pkgver = "6.9.0"
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
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/prison-{pkgver}.tar.xz"
sha256 = "e84135473756a7b6cdfcbc026b464112dc02c158550ec3149b308e065a798443"
hardening = ["vis"]


def post_install(self):
    self.install_license("LICENSES/MIT.txt")


@subpackage("prison-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
