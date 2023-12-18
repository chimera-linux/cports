pkgname = "python-rencode"
pkgver = "1.0.6"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-cython",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
makedepends = ["python-devel"]
depends = ["python"]
pkgdesc = "Python object serialization library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://github.com/aresch/rencode"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "0ed61111f053ea37511da86ca7aed2a3cfda6bdaa1f54a237c4b86eea52f0733"
# FIXME: can't import pythonpath/rencode/_rencode.py when $cwd/rencode already
# exists (precedence)
options = ["!check"]
