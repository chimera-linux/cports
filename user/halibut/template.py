pkgname = "halibut"
pkgver = "1.3"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "perl"]
pkgdesc = "Yet another free document preparation system"
maintainer = "Earldridge Jazzed Pineda <earldridgejazzedpineda@gmail.com>"
license = "MIT AND APAFML"
url = "https://www.chiark.greenend.org.uk/~sgtatham/halibut"
source = f"{url}/halibut-{pkgver}/halibut-{pkgver}.tar.gz"
sha256 = "aaa0f7696f17f74f42d97d0880aa088f5d68ed3079f3ed15d13b6e74909d3132"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENCE")
