pkgname = "python-configargparse"
pkgver = "1.7.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python"]
checkdepends = ["python-pytest", "python-pyyaml"]
pkgdesc = "Drop-in replacement for argparse"
license = "MIT"
url = "https://github.com/bw2/ConfigArgParse"
source = f"$(PYPI_SITE)/C/ConfigArgParse/configargparse-{pkgver}.tar.gz"
sha256 = "79c2ddae836a1e5914b71d58e4b9adbd9f7779d4e6351a637b7d2d9b6c46d3d9"
# needs updating for 3.13
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
