pkgname = "ansible-core"
pkgver = "2.17.4"
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
sha256 = "44a1f30076796536ba2455cad18d36e62870f04e632e3ca2ebe970d7beacf24d"


def check(self):
    self.do(
        "./bin/ansible-test",
        "units",
    )
