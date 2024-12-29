pkgname = "pgp2ssh"
pkgver = "0_git20240601"
pkgrel = 0
_commit = "815c00db15664512705f7cb7b36469b099fdc3eb"
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Convert PGP/GPG private keys to SSH private keys"
maintainer = "as400 <as400@smail.net.pl>"
license = "MIT"
url = "https://github.com/pinpox/pgp2ssh"
source = f"{url}/archive/{_commit}.tar.gz"
sha256 = "4f9b0377c8876f45f86a6bb8fe567eb62f3088ef51b41b9c1b71805fa5b693ec"


def post_install(self):
    self.install_license("LICENSE")
