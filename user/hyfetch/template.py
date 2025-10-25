pkgname = "hyfetch"
pkgver = "2.0.4"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
depends = ["bash"]
pkgdesc = "Neofetch with pride flags"
license = "MIT"
url = "https://github.com/hykilpikonna/hyfetch"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "8de8908334470f24dfae5693bd9660360ec8c1074b270f36eac659530e0b35ba"
# no test
options = ["!check"]


def install(self):
    self.cargo.install(wrksrc="crates/hyfetch")
    self.install_bin("neofetch", name="neowofetch")

    self.install_license("LICENSE.md")
    self.install_man("docs/hyfetch.1")

    for shell in ["bash", "zsh"]:
        self.install_completion(f"hyfetch/scripts/autocomplete.{shell}", shell)
