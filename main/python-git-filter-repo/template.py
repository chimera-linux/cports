pkgname = "python-git-filter-repo"
pkgver = "2.47.0"
pkgrel = 0
build_style = "python_pep517"
make_build_env = {"SETUPTOOLS_SCM_PRETEND_VERSION": pkgver}
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools_scm",
]
depends = ["git", "python"]
checkdepends = ["bash", "rsync", *depends]
pkgdesc = "Tool for rewriting git history"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://github.com/newren/git-filter-repo"
# pypi tarball doesn't contain man page
source = f"{url}/releases/download/v{pkgver}/git-filter-repo-{pkgver}.tar.xz"
sha256 = "4662cbe5918196a9f1b5b3e1211a32e61cff1812419c21df4f47c5439f09e902"
# TODO: figure out why some of the tests fail
options = ["!check"]


def check(self):
    self.do("../t/run_tests")


def post_install(self):
    self.install_license("COPYING.mit")
    self.install_man("Documentation/man1/git-filter-repo.1")
