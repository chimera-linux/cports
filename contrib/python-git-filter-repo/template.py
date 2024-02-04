pkgname = "python-git-filter-repo"
pkgver = "2.38.0"
pkgrel = 0
build_wrksrc = "release"
build_style = "python_pep517"
make_build_env = {"SETUPTOOLS_SCM_PRETEND_VERSION": pkgver}
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools_scm",
    "python-wheel",
]
depends = ["git", "python"]
checkdepends = ["bash", "rsync"] + depends
pkgdesc = "Tool for rewriting git history"
maintainer = "miko <mikoxyzzz@gmail.com>"
license = "MIT"
url = "https://github.com/newren/git-filter-repo"
# pypi tarball doesn't contain tests and man pages
source = f"{url}/releases/download/v{pkgver}/git-filter-repo-{pkgver}.tar.xz"
sha256 = "db954f4cae9e47c6be3bd3161bc80540d44f5379cb9cf9df498f4e019f0a41a9"
# TODO: figure out why some of the tests fail
options = ["!check"]


def do_check(self):
    self.do("../t/run_tests")


def post_install(self):
    self.install_license("../COPYING.mit")
    self.install_man("../Documentation/man1/git-filter-repo.1")
