pkgname = "keychain"
pkgver = "2.9.8"
pkgrel = 0
build_style = "makefile"
hostmakedepends = ["perl"]
pkgdesc = "Manager for ssh-agent and gpg-agent"
license = "GPL-2.0-or-later"
url = "https://github.com/funtoo/keychain"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "589cf55ae5c4b65af1d977d705beb319006efca5bcdda8352b8558d0dcff5a84"
# no tests
options = ["!check"]


def install(self):
    self.make.build()
    self.install_bin("keychain")
    self.install_man("keychain.1")
