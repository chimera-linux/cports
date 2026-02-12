pkgname = "croc"
pkgver = "10.2.7"
pkgrel = 2
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "File transfer tool"
license = "MIT"
url = "https://github.com/schollz/croc"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "eea957c840041e11cc214b5f9c31801b0f8b51621d6629b89ba5743788d8e7c6"
# check: needs network access
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_completion("src/install/bash_autocomplete", "bash")
    self.install_completion("src/install/zsh_autocomplete", "zsh")
