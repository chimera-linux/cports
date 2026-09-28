pkgname = "croc"
pkgver = "11.0.2"
pkgrel = 1
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "File transfer tool"
license = "MIT"
url = "https://github.com/schollz/croc"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "833c4cb804d1ebdca4594803d0bba05f5bd8663a148fa3ee9c55e3184c805abb"
# check: needs network access
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_completion("src/install/bash_autocomplete", "bash")
    self.install_completion("src/install/zsh_autocomplete", "zsh")
