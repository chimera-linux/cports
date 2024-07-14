pkgname = "python-argcomplete"
pkgver = "3.4.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-setuptools_scm",
    "python-wheel",
]
depends = ["python"]
checkdepends = ["bash", "python-pexpect", "python-pip", "zsh"]
pkgdesc = "Python tab completion plugin"
maintainer = "psykose <alice@ayaya.dev>"
license = "Apache-2.0"
url = "https://github.com/kislyuk/argcomplete"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "a66504125897239587a5422e31535698704baa67d54604557b17176d56bc69bd"


def init_build(self):
    self.env["SETUPTOOLS_SCM_PRETEND_VERSION"] = pkgver


def do_check(self):
    self.do("python", "-m", "unittest", "-b", "test/test.py")
