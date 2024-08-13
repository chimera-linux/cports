pkgname = "croc"
pkgver = "10.0.11"
pkgrel = 2
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "File transfer tool"
maintainer = "Paul A. Patience <paul@apatience.com>"
license = "MIT"
url = "https://github.com/schollz/croc"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "09b355bb412d9b5d1b2e0c30b866b9885fe6c4e88f65f6486d1f0233d591e07d"
# check: needs network access
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_completion("src/install/bash_autocomplete", "bash")
    self.install_completion("src/install/zsh_autocomplete", "zsh")
