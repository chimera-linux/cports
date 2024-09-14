pkgname = "python-git-filter-repo"
pkgver = "2.45.0"
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
sha256 = "430a2c4a5d6f010ebeafac6e724e3d8d44c83517f61ea2b2d0d07ed8a6fc555a"
# TODO: figure out why some of the tests fail
options = ["!check"]


def check(self):
    self.do("../t/run_tests")


def post_install(self):
    self.install_license("COPYING.mit")
    self.install_man("Documentation/man1/git-filter-repo.1")
