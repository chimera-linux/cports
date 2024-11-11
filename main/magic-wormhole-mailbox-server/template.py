pkgname = "magic-wormhole-mailbox-server"
pkgver = "0.5.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = [
    "python-attrs",
    "python-autobahn",
    "python-twisted",
]
checkdepends = [
    "python-mock",
    "python-pytest",
    "python-treq",
    *depends,
]
pkgdesc = "Rendezvous/mailbox server for Magic Wormhole clients"
maintainer = "triallax <triallax@tutanota.com>"
license = "MIT"
url = "https://github.com/magic-wormhole/magic-wormhole-mailbox-server"
source = f"$(PYPI_SITE)/m/magic-wormhole-mailbox-server/magic-wormhole-mailbox-server-{pkgver}.tar.gz"
sha256 = "a007a03672293204657681dbf502045d6d5817c57f9aae2f2226e6ea1a008ca1"


def post_install(self):
    self.install_license("LICENSE")
