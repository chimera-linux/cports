pkgname = "python-rencode"
pkgver = "1.0.8"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-cython",
    "python-installer",
    "python-poetry-core",
    "python-setuptools",
    "python-wheel",
]
makedepends = ["python-devel"]
depends = ["python"]
pkgdesc = "Python object serialization library"
license = "GPL-3.0-or-later"
url = "https://github.com/aresch/rencode"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "480aab74948a7f339b749b5c39bdb4caf15429f4b49a998c770d5f371098d351"
# FIXME: can't import pythonpath/rencode/_rencode.py when $cwd/rencode already
# exists (precedence)
options = ["!check"]


def build(self):
    self.do("pyproject-build", "--no-isolation", "--wheel", ".")
