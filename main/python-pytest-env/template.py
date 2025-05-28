pkgname = "python-pytest-env"
pkgver = "1.1.5"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-hatch_vcs",
    "python-hatchling",
    "python-installer",
]
depends = ["python-pytest"]
checkdepends = [*depends]
pkgdesc = "Pytest plugin for adding environment variables"
license = "MIT"
url = "https://github.com/pytest-dev/pytest-env"
source = f"$(PYPI_SITE)/p/pytest-env/pytest_env-{pkgver}.tar.gz"
sha256 = "91209840aa0e43385073ac464a554ad2947cc2fd663a9debf88d03b01e0cc1cf"


def post_install(self):
    self.install_license("LICENSE")
