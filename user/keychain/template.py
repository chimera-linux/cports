pkgname = "keychain"
pkgver = "2.9.5"
pkgrel = 0
build_style = "makefile"
hostmakedepends = ["perl"]
pkgdesc = "Manager for ssh-agent and gpg-agent"
license = "GPL-2.0-or-later"
url = "https://github.com/funtoo/keychain"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "c883f26db616bc1c81ba5ef3832c7ad912f3e8bd0baf6aaff981164c538a1411"
# no tests
options = ["!check"]


def install(self):
    self.make.build()
    self.install_bin("keychain")
    self.install_man("keychain.1")
