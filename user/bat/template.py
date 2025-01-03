pkgname = "bat"
pkgver = "0.24.0"
pkgrel = 2
build_style = "cargo"
prepare_after_patch = True
make_build_env = {"BAT_ASSETS_GEN_DIR": "gen"}
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = [
    "libgit2-devel",
    "oniguruma-devel",
    "rust-std",
    "zlib-ng-compat-devel",
]
checkdepends = ["bash"]
pkgdesc = "Cat clone but larger"
maintainer = "aurelia <git@elia.garden>"
license = "MIT OR Apache-2.0"
url = "https://github.com/sharkdp/bat"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "907554a9eff239f256ee8fe05a922aad84febe4fe10a499def72a4557e9eedfb"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/bat")
    self.install_man("gen/assets/manual/bat.1")
    self.install_license("LICENSE-MIT")
    self.install_completion("gen/assets/completions/bat.bash", "bash")
    self.install_completion("gen/assets/completions/bat.fish", "fish")
    self.install_completion("gen/assets/completions/bat.zsh", "zsh")
