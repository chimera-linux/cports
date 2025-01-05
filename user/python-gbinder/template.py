pkgname = "python-gbinder"
pkgver = "1.1.2"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "pkgconf",
    "python-build",
    "python-cython",
    "python-installer",
    "python-setuptools",
]
makedepends = [
    "libgbinder-devel",
    "python-devel",
]
pkgdesc = "Python bindings for libgbinder"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://github.com/erfanoabdi/gbinder-python"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "2dc424d5c2594146612e4bd752964f8928a62eec7c5ce6046f4c582079d0b537"
# check: needs manually running script in .py with manual setup
options = ["!check"]
