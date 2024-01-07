pkgname = "python-sphinxcontrib-serializinghtml"
pkgver = "1.1.5"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
checkdepends = ["python-sphinx"]
depends = ["python"]
pkgdesc = "Sphinx extension which outputs serialized HTML document"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "http://sphinx-doc.org"
source = f"$(PYPI_SITE)/s/sphinxcontrib-serializinghtml/sphinxcontrib-serializinghtml-{pkgver}.tar.gz"
sha256 = "aa5f6de5dfdf809ef505c4895e51ef5c9eac17d0f287933eb49ec495280b6952"
# circular checkdepends
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
