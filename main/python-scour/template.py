pkgname = "python-scour"
pkgver = "0.38.2"
pkgrel = 2
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python-six"]
checkdepends = ["python-pytest"] + depends
pkgdesc = "Python SVG scrubber"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://github.com/scour-project/scour"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "26166de53d9da3eccc52570bf8c2853e60efefd9e90e26fdfc7124fe0bd873af"
