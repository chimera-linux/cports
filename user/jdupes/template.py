pkgname = "jdupes"
pkgver = "1.28.0"
pkgrel = 0
build_style = "makefile"
make_dir = "."
make_check_target = "test"
makedepends = [
    "libjodycode-devel-static",
]
depends = ["libjodycode-devel", "xxhash"]
pkgdesc = "Identifying and taking actions upon duplicate files"
license = "MIT"
url = "https://codeberg.org/jbruchon/jdupes"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "a8f21c04fff5e3ff0a92e8ac76114b2195ed43dc32b84bf343f5256e7ba9cb04"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")
