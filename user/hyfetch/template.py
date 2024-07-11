pkgname = "hyfetch"
pkgver = "1.4.11"
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
sha256 = "79cd6706a681fa7c05754b35d9338abf96bebce222c27376a4155e94d6a5350d"
# no test
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.md")
    self.install_man("docs/hyfetch.1")

    for shell in ["bash", "zsh"]:
        self.install_completion(f"hyfetch/scripts/autocomplete.{shell}", shell)
