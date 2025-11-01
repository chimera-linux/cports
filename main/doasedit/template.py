pkgname = "doasedit"
pkgver = "1.0.9"
pkgrel = 0
build_style = "makefile"
make_install_args = ["prefix=/usr"]
depends = ["opendoas"]
pkgdesc = "Shell script to edit files with doas"
license = "MIT"
url = "https://codeberg.org/TotallyLeGIT/doasedit"
source = f"https://codeberg.org/TotallyLeGIT/doasedit/archive/{pkgver}.tar.gz"
sha256 = "bb02ab7a86b44f9128f6216946c8d21b41a1a4cc9acc06055d4774105a2239ee"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
