pkgname = "python-b4"
pkgver = "0.14.1"
pkgrel = 0
build_style = "python_pep517"
# it tries to run the tests from the build dir if we don't do this...
make_check_args = ["src/tests"]
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = [
    "python-dkimpy",
    "python-dnspython",
    "python-git-filter-repo",
    "python-patatt",
    "python-requests",
]
checkdepends = ["python-git-filter-repo", "python-pytest", "python-requests"]
pkgdesc = "Tool to help with email-based patch workflows"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://github.com/mricon/b4"
# pypi tarball doesn't contain tests
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "c2c679ca223f5814196714dc0c7a2aeb7f4740e49a7878f4c00a3d8963c7f14b"
