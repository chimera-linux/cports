pkgname = "ansible-core"
pkgver = "2.19.2"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = [
    "python-cryptography",
    "python-jinja2",
    "python-packaging",
    "python-passlib",
    "python-pyyaml",
    "python-resolvelib",
]
checkdepends = [
    "git",
    "openssh",
    "python-bcrypt",
    "python-pytest",
    "python-pytest-mock",
    "python-pytest-xdist",
    "util-linux-mount",
    *depends,
]
pkgdesc = "Configuration management and multinode orchestration framework"
subdesc = "core components"
license = "GPL-3.0-or-later"
url = "https://ansible.com"
# pypi does not ship some files
source = (
    f"https://github.com/ansible/ansible/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "cb3feaf0edb3e3e70a4483f4990edb5935066d87de9d99a65bfdef5db9b4976c"


def check(self):
    self.do(
        "./bin/ansible-test",
        "units",
    )
