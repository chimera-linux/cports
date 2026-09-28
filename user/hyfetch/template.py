pkgname = "hyfetch"
pkgver = "2.1.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
depends = ["bash"]
pkgdesc = "Neofetch with pride flags"
license = "MIT"
url = "https://github.com/hykilpikonna/hyfetch"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "23e3600093de3daa60dbbfd1edff258504f41f0fcfcb5537ddff78711b0d2eb2"
# no test
options = ["!check"]


def install(self):
    self.cargo.install(wrksrc="crates/hyfetch")
    self.install_bin("neofetch", name="neowofetch")

    self.install_license("LICENSE.md")
    self.install_man("docs/hyfetch.1")

    for shell in ["bash", "zsh"]:
        self.install_completion(f"hyfetch/scripts/autocomplete.{shell}", shell)
