pkgname = "magic-wormhole-mailbox-server"
pkgver = "0.4.1"
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
sha256 = "1af10592909caaf519c00e706eac842c5e77f8d4356215fe9c61c7b2258a88fb"


def post_install(self):
    self.install_license("LICENSE")
