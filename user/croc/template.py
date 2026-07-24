pkgname = "croc"
pkgver = "10.6.0"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "File transfer tool"
license = "MIT"
url = "https://github.com/schollz/croc"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "d9ee32d93e8353fd4330d71ee2683f08e22f4a58b2f3f5a73c1c9d622ffd4598"
# check: needs network access
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_completion("src/install/bash_autocomplete", "bash")
    self.install_completion("src/install/zsh_autocomplete", "zsh")
