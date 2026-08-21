pkgname = "prison"
pkgver = "6.29.0"
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
sha256 = "8d34da7a7a55d35bcc5824245e2dbec2611977d164d57bef2dcccee6004443a7"
hardening = ["vis"]


def post_install(self):
    self.install_license("LICENSES/MIT.txt")


@subpackage("prison-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
