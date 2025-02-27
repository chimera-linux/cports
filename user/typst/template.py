pkgname = "typst"
pkgver = "0.13.0"
pkgrel = 0
build_style = "cargo"
make_build_args = ["-p", "typst-cli"]
make_build_env = {
    "TYPST_VERSION": f"{pkgver}",
    "GEN_ARTIFACTS": "./generated",
}
make_check_args = ["-p", "typst-cli"]
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["rust-std", "openssl3-devel"]
pkgdesc = "Markup-based typesetting system"
license = "Apache-2.0"
url = "https://typst.app"
source = f"https://github.com/typst/typst/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "5a7224e32a555ac647ff202667a183b80d35539b685b3ce64bedf5d4e5a1a286"
# takes forever
options = ["!check"]


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/typst")
    with self.pushd("crates/typst-cli/generated"):
        self.install_man("typst*.1", glob=True)
        self.install_completion("typst.bash", "bash")
        self.install_completion("typst.fish", "fish")
        self.install_completion("_typst", "zsh")
