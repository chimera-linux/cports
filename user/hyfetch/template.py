pkgname = "hyfetch"
pkgver = "2.1.1"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
depends = ["bash"]
pkgdesc = "Neofetch with pride flags"
license = "MIT"
url = "https://github.com/hykilpikonna/hyfetch"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "d83708caafa560531ee9dea002aa58123272a0209b4e6b296bae34c87665004a"
# no test
options = ["!check"]


def install(self):
    self.cargo.install(wrksrc="crates/hyfetch")
    self.install_bin("neofetch", name="neowofetch")

    self.install_license("LICENSE.md")
    self.install_man("docs/hyfetch.1")

    for shell in ["bash", "zsh"]:
        self.install_completion(f"hyfetch/scripts/autocomplete.{shell}", shell)
