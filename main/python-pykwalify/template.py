pkgname = "python-pykwalify"
pkgver = "1.8.0"
pkgrel = 1
build_style = "python_pep517"
make_check_args = [
    # needs 'testfixtures'
    "--ignore=tests/test_core.py",
    "--ignore=tests/test_unicode.py",
]
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = [
    "python-dateutil",
    "python-docopt",
    "python-ruamel.yaml",
]
checkdepends = ["python-pytest", *depends]
pkgdesc = "YAML/JSON schema validation for python"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://github.com/Grokzen/pykwalify"
source = f"$(PYPI_SITE)/p/pykwalify/pykwalify-{pkgver}.tar.gz"
sha256 = "796b2ad3ed4cb99b88308b533fb2f559c30fa6efb4fa9fda11347f483d245884"


def post_install(self):
    self.install_license("LICENSE")
