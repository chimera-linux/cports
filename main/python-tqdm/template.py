pkgname = "python-tqdm"
pkgver = "4.67.0"
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
sha256 = "fe5a6f95e6fe0b9755e9469b77b9c3cf850048224ecaa8293d7d2d31f97d869a"


def init_check(self):
    self.make_check_args += [f"--numprocesses={self.make_jobs}"]


def post_install(self):
    self.install_license("LICENCE")
    self.install_completion("tqdm/completion.sh", "bash", "tqdm")
    self.install_man("tqdm/tqdm.1")
