pkgname = "croc"
pkgver = "9.6.13"
pkgrel = 1
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "File transfer tool"
maintainer = "Paul A. Patience <paul@apatience.com>"
license = "MIT"
url = "https://github.com/schollz/croc"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "5362ae8433ebd4fda9efcd853b4b8959992cf5f531ef0958ea6ed969f2eafa7b"
# debug: fails to split on powerpc
# check: needs network access
options = ["!debug", "!check"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_completion("src/install/bash_autocomplete", "bash")
    self.install_completion("src/install/zsh_autocomplete", "zsh")
