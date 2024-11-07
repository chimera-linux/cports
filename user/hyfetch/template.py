pkgname = "hyfetch"
pkgver = "1.99.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = [
    "bash",
    "python-setuptools",
]
pkgdesc = "Neofetch with pride flags"
maintainer = "cassiofb-dev <contact@cassiofernando.com>"
license = "MIT"
url = "https://github.com/hykilpikonna/hyfetch"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "c712a11a354b34a86c86e7b080ee5e63faa6db5b8a88a3ebea35ef67c33588fd"
# no test
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.md")
    self.install_man("docs/hyfetch.1")

    for shell in ["bash", "zsh"]:
        self.install_completion(f"hyfetch/scripts/autocomplete.{shell}", shell)
