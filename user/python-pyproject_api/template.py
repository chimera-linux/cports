pkgname = "python-pyproject_api"
pkgver = "1.9.1"
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
sha256 = "43c9918f49daab37e302038fc1aed54a8c7a91a9fa935d00b9a485f37e0f5335"


def post_install(self):
    self.install_license("LICENSE")
