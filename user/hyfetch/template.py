pkgname = "hyfetch"
pkgver = "2.0.2"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
depends = ["bash"]
pkgdesc = "Neofetch with pride flags"
license = "MIT"
url = "https://github.com/hykilpikonna/hyfetch"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "051acbb25a60ac57e8a8b43159f032a9bcec9b25cd1ed7854899f6ad3bcbd6d5"
# no test
options = ["!check"]


def install(self):
    self.cargo.install(wrksrc="crates/hyfetch")
    self.install_bin("neofetch", name="neowofetch")

    self.install_license("LICENSE.md")
    self.install_man("docs/hyfetch.1")

    for shell in ["bash", "zsh"]:
        self.install_completion(f"hyfetch/scripts/autocomplete.{shell}", shell)
