pkgname = "ansible-core"
pkgver = "2.20.5"
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
sha256 = "45fbc904f160c5ae192f72553e8ccada3d2ef90f40ff69d3e9c2fda016b9b745"


def check(self):
    self.do(
        "./bin/ansible-test",
        "units",
    )
