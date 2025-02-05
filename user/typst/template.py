pkgname = "typst"
pkgver = "0.12.0"
pkgrel = 1
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
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "Apache-2.0"
url = "https://typst.app"
source = f"https://github.com/typst/typst/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "5e92463965c0cf6aa003a3bacd1c68591ef2dc0db59dcdccb8f7b084836a1266"
# takes forever
options = ["!check"]


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/typst")
    with self.pushd("crates/typst-cli/generated"):
        self.install_man("typst*.1", glob=True)
        self.install_completion("typst.bash", "bash")
        self.install_completion("typst.fish", "fish")
        self.install_completion("_typst", "zsh")
