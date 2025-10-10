pkgname = "python-pyproject_api"
pkgver = "1.10.0"
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
sha256 = "40c6f2d82eebdc4afee61c773ed208c04c19db4c4a60d97f8d7be3ebc0bbb330"


def post_install(self):
    self.install_license("LICENSE")
