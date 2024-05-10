pkgname = "python-jinja2"
pkgver = "3.1.4"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-flit_core",
    "python-installer",
]
checkdepends = ["python-pytest", "python-markupsafe"]
depends = ["python", "python-markupsafe"]
pkgdesc = "Python template engine"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://jinja.palletsprojects.com"
source = f"$(PYPI_SITE)/J/Jinja2/jinja2-{pkgver}.tar.gz"
sha256 = "4a3aee7acbbe7303aede8e9648d13b8bf88a429282aa6122a993f0ac800cb369"
# dependency of pytest
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")
