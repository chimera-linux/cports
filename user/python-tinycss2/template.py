pkgname = "python-tinycss2"
pkgver = "1.3.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = ["python-build", "python-flit_core", "python-installer"]
depends = ["python-webencodings"]
checkdepends = ["python-pytest", *depends]
pkgdesc = "Tiny CSS parser"
maintainer = "Earldridge Jazzed Pineda <earldridgejazzedpineda@gmail.com>"
license = "BSD-3-Clause"
url = "https://github.com/Kozea/tinycss2"
source = [
    f"{url}/archive/refs/tags/v{pkgver}.tar.gz",
    "https://github.com/CourtBouillon/css-parsing-tests/archive/43e65b244133f17eb8a4d4404d5774672b94824f.tar.gz",
]
source_paths = [".", "tests/css-parsing-tests"]
sha256 = [
    "e085126b6223786cb56dc711d460f7d8a9e425ad93d01bd6d5ecc08ede6bc846",
    "5ce8e00cb8e66bde6cad50e6c12463600d94cbe2d6ec2dbb746ebcbff2ecf9d4",
]


def post_install(self):
    self.install_license("LICENSE")
