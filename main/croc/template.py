pkgname = "croc"
pkgver = "10.1.3"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "File transfer tool"
maintainer = "Paul A. Patience <paul@apatience.com>"
license = "MIT"
url = "https://github.com/schollz/croc"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "3bce38e7d74714bb7ca00791ee9771935a4d2c5dac8a8831b6713f49c1ec4207"
# check: needs network access
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_completion("src/install/bash_autocomplete", "bash")
    self.install_completion("src/install/zsh_autocomplete", "zsh")
