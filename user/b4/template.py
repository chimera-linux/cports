pkgname = "b4"
pkgver = "0.16.0"
pkgrel = 0
build_style = "python_pep517"
make_check_args = [
    # tries to run tests from the build dir
    "src/tests",
]
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = [
    "python-aiodns",
    "python-dkimpy",
    "python-dnspython",
    "python-ezgb",
    "python-git-filter-repo",
    "python-liblore",
    "python-patatt",
    "python-pygit2",
    "python-requests",
    # optional, TODO
    # "python-textual",
]
checkdepends = [
    "python-pytest",
    *depends,
]
renames = ["python-b4"]
pkgdesc = "Tool to help with email-based patch workflows"
license = "GPL-2.0-or-later"
url = "https://github.com/mricon/b4"
# pypi tarball doesn't contain tests
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "56dd7e8953d50cb316e1ff3193d1bcba521f298e38722999c64c31847dc9b1d6"
