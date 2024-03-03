pkgname = "python-pytest-env"
pkgver = "1.1.3"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-hatchling",
    "python-hatch_vcs",
]
depends = ["python-pytest"]
checkdepends = list(depends)
pkgdesc = "Pytest plugin for adding environment variables"
maintainer = "Duncan Bellamy <dunk@denkimushi.com>"
license = "MIT"
url = "https://github.com/MobileDynasty/pytest-env"
source = f"$(PYPI_SITE)/p/pytest-env/pytest_env-{pkgver}.tar.gz"
sha256 = "fcd7dc23bb71efd3d35632bde1bbe5ee8c8dc4489d6617fb010674880d96216b"


def post_install(self):
    self.install_license("LICENSE")
