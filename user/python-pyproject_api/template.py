pkgname = "python-pyproject_api"
pkgver = "1.9.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-hatch_vcs",
    "python-hatchling",
    "python-installer",
]
checkdepends = ["python-pytest-mock"]
depends = ["python"]
pkgdesc = "API to interact with the python pyproject.toml based projects"
license = "MIT"
url = "https://pypi.org/project/pyproject-api"
source = f"$(PYPI_SITE)/p/pyproject_api/pyproject_api-{pkgver}.tar.gz"
sha256 = "7e8a9854b2dfb49454fae421cb86af43efbb2b2454e5646ffb7623540321ae6e"


def post_install(self):
    self.install_license("LICENSE")
