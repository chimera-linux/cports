pkgname = "ansible-core"
pkgver = "2.17.6"
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
sha256 = "3e53970b7cebfe2adb39b711c1e2f8bbfcbedac828da51dc0357a19070638e95"


def check(self):
    self.do(
        "./bin/ansible-test",
        "units",
    )
