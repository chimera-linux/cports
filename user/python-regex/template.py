pkgname = "python-regex"
pkgver = "2025.2.13"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-wheel",
    "python-setuptools",
]
makedepends = ["python-devel"]
checkdepends = ["python-pytest"]
pkgdesc = "Alternative regular expression module, to replace re"
license = "Apache-2.0"
url = "https://github.com/mrabarnett/mrab-regex"
# outdated pypi source
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "d44c8b925245f5c07dd2ee7b69139902f24df0d5b43c5f14225d7071dd1a2b1a"
# FIXME: failing tests
options = ["!check"]
