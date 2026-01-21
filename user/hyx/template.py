pkgname = "hyx"
pkgver = "2024.02.29"
pkgrel = 0
build_style = "makefile"
pkgdesc = "Terminal hex editor inspired by vim"
license = "MIT"
url = "https://yx7.cc/code"
source = f"https://yx7.cc/code/hyx/hyx-{pkgver}.tar.xz"
sha256 = "76e7f1df3b1a6de7aded1a7477ad0c22e36a8ac21077a52013b5836583479771"

# hyx has no check step
options = ["!check"]

def install(self):
    self.install_bin("hyx")
    self.install_license("license.txt")
