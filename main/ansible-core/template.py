pkgname = "ansible-core"
pkgver = "2.17.5"
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
    "python-pytest",
    "python-pytest-mock",
    "python-pytest-xdist",
    *depends,
]
pkgdesc = "Configuration management and multinode orchestration framework"
subdesc = "core components"
maintainer = "Mara <177581589+catgirlconspiracy@users.noreply.github.com>"
license = "GPL-3.0-or-later"
url = "https://ansible.com"
source = f"$(PYPI_SITE)/a/ansible-core/ansible_core-{pkgver}.tar.gz"
sha256 = "ae7f51fd13dc9d57c9bcd43ef23f9c255ca8f18f4b5c0011a4f9b724d92c5a8e"


def check(self):
    self.do(
        "./bin/ansible-test",
        "units",
    )
