pkgname = "pgp2ssh"
pkgver = "0.1"
pkgrel = 0
archs = ["x86_64"]
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Convert PGP/GPG private keys to SSH private keys"
maintainer = "as400 <as400@smail.net.pl>"
license = "MIT"
url = "https://github.com/pinpox/pgp2ssh"
source = f"{url}/archive/refs/heads/main.tar.gz"
sha256 = "19f0b1d1952fac9f2e5db9914d1352b9c496c6d72a12deecf9b028147408c550"


def post_install(self):
    self.install_license("LICENSE")
