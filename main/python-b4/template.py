pkgname = "python-b4"
pkgver = "0.14.2"
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
sha256 = "ba79ca0a67f106f20e3d10db8a63bc8097deb4c33ea1f00a90496ea00b985783"
