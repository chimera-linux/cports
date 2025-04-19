pkgname = "python-pylama"
pkgver = "8.4.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-wheel",
    "python-setuptools",
]
depends = [
    "python-mccabe",
    "python-pycodestyle",
    "python-pyflakes",
]
checkdepends = [
    "python-eradicate",
    "python-mypy",
    "python-pylama-quotes",
    "python-pylint",
    "python-pytest",
    "python-pytest-mypy",
    "python-radon",
    "python-toml",
    "python-vulture",
]
checkdepends = ["python-pytest"]
pkgdesc = "Code audit tool for python"
license = "MIT"
url = "https://github.com/klen/pylama"
source = f"$(PYPI_SITE)/p/pylama/pylama-{pkgver}.tar.gz"
sha256 = "2d4f7aecfb5b7466216d48610c7d6bad1c3990c29cdd392ad08259b161e486f6"
# FIXME
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
