pkgname = "croc"
pkgver = "11.5.4"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "File transfer tool"
license = "MIT"
url = "https://github.com/schollz/croc"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "16910b594704b40e9df35eb3bc637db675fe3d770a4588bd32b5a12c5ff174ff"
# check: needs network access
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_completion("src/install/bash_autocomplete", "bash")
    self.install_completion("src/install/zsh_autocomplete", "zsh")
