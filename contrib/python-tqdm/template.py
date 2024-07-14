pkgname = "python-tqdm"
pkgver = "4.66.4"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools_scm",
]
depends = ["python"]
checkdepends = [
    "python-numpy",
    "python-pytest-asyncio",
    "python-pytest-timeout",
    "python-pytest-xdist",
]
pkgdesc = "Python progress bar"
maintainer = "triallax <triallax@tutanota.com>"
license = "MIT AND MPL-2.0"
url = "https://tqdm.github.io"
source = f"$(PYPI_SITE)/t/tqdm/tqdm-{pkgver}.tar.gz"
sha256 = "e4d936c9de8727928f3be6079590e97d9abfe8d39a590be678eb5919ffc186bb"


def init_check(self):
    self.make_check_args += [f"--numprocesses={self.make_jobs}"]


def post_install(self):
    self.install_license("LICENCE")
    self.install_completion("tqdm/completion.sh", "bash", "tqdm")
    self.install_man("tqdm/tqdm.1")
