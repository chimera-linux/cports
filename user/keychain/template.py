pkgname = "keychain"
pkgver = "3.0.8"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
checkdepends = ["python-pytest"]
pkgdesc = "Manager for ssh-agent and gpg-agent"
license = "GPL-3.0-or-later"
url = "https://github.com/funtoo/keychain"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "66bf1a3e3887b924a7649fbf4a72b4982a5345fdfb634ffffd772085e2ba72da"


def post_build(self):
    self.do("make", "keychain.1")


def post_install(self):
    self.install_man("keychain.1")
