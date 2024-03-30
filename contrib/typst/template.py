pkgname = "typst"
pkgver = "0.11.0"
pkgrel = 0
build_wrksrc = "crates/typst-cli"
build_style = "cargo"
make_build_env = {
    "TYPST_VERSION": f"{pkgver}",
    "GEN_ARTIFACTS": "./generated",
}
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["rust-std", "openssl-devel"]
pkgdesc = "Markup-based typesetting system"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "Apache-2.0"
url = "https://typst.app"
source = f"https://github.com/typst/typst/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "fd8debe21d5d22d4cd6c823494537f1356c9954cc2fe6c5db8c76c1b126112dd"


def do_install(self):
    self.install_bin(f"../../target/{self.profile().triplet}/release/typst")
    self.install_man("generated/typst*.1", glob=True)
    self.install_completion("generated/typst.bash", "bash")
    self.install_completion("generated/typst.fish", "fish")
    self.install_completion("generated/_typst", "zsh")
