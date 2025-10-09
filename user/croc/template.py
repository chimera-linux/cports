pkgname = "croc"
pkgver = "10.2.5"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "File transfer tool"
license = "MIT"
url = "https://github.com/schollz/croc"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "993e0bb72e79c5168d78db5c14d84f69beeab819ab4d06f4d98fcddd23487207"
# check: needs network access
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_completion("src/install/bash_autocomplete", "bash")
    self.install_completion("src/install/zsh_autocomplete", "zsh")
