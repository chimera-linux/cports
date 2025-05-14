pkgname = "python-automat"
pkgver = "25.4.16"
pkgrel = 0
build_style = "python_pep517"
make_build_env = {"SETUPTOOLS_SCM_PRETEND_VERSION": pkgver}
hostmakedepends = [
    "python-build",
    "python-hatch_vcs",
    "python-installer",
    "python-setuptools_scm",
]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Finite state machines for Python"
license = "MIT"
url = "https://github.com/glyph/Automat"
source = f"$(PYPI_SITE)/A/Automat/automat-{pkgver}.tar.gz"
sha256 = "0017591a5477066e90d26b0e696ddc143baafd87b588cfac8100bc6be9634de0"


def check(self):
    self.do("pytest", "src/automat/_test")


def post_install(self):
    self.install_license("LICENSE")
