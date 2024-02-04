pkgname = "python-b4"
pkgver = "0.12.4"
pkgrel = 0
build_style = "python_pep517"
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
maintainer = "miko <mikoxyzzz@gmail.com>"
license = "GPL-2.0-or-later"
url = "https://github.com/mricon/b4"
# pypi tarball doesn't contain tests
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "a983ff0681cedd2d7d49f7371fd7b8ca5d142bbb4e3756cc995cd31817df13a5"
