pkgname = "python-pygls"
pkgver = "1.3.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-poetry-core",
]
depends = [
    "python-cattrs",
    "python-lsprotocol",
]
checkdepends = [
    "python-pytest-asyncio",
    "python-pytest-xdist",
    *depends,
]
pkgdesc = "Language server protocol framework for Python"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "Apache-2.0"
url = "https://pygls.readthedocs.io/en/latest"
# no tests in pypi
source = f"https://github.com/openlawlibrary/pygls/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "d2dc2b8e298cac8d3945b237cff1f103b0bf6349f0308361b0041dcdae59ab2f"


def init_check(self):
    self.make_check_args = [
        f"--numprocesses={self.make_jobs}",
        "--dist=worksteal",
    ]
