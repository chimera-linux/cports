pkgname = "python-pygls"
pkgver = "2.0.0"
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
license = "Apache-2.0"
url = "https://pygls.readthedocs.io/en/latest"
# no tests in pypi
source = f"https://github.com/openlawlibrary/pygls/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "33f28ac94aef0b40097f21205531ba35e95caf86fca4d553854d35ec964915f6"


def init_check(self):
    self.make_check_args = [
        f"--numprocesses={self.make_jobs}",
        "--dist=worksteal",
    ]
