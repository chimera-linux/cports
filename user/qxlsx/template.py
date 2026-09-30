pkgname = "qxlsx"
pkgver = "1.5.1.1"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_SHARED_LIBS=ON"]
cmake_dir = "QXlsx"
hostmakedepends = [
    "cmake",
    "ninja",
]
makedepends = [
    "qt6-qtbase-devel",
    "qt6-qtbase-private-devel",
]
pkgdesc = "Excel file library using Qt"
license = "MIT"
url = "https://qtexcel.github.io/QXlsx"
source = f"https://github.com/QtExcel/QXlsx/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "70e424ad47529e16cd8ad1bad2ccc561af1eb50ef8ee45f1b50cb277f9a12730"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("qxlsx-devel")
def _(self):
    return self.default_devel()
