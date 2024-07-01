pkgname = "bat"
pkgver = "0.24.0"
pkgrel = 0
build_style = "cargo"
make_build_env = {"BAT_ASSETS_GEN_DIR": "gen"}
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = [
    "rust-std",
    "oniguruma-devel",
    "libgit2-devel",
    "zlib-ng-compat-devel",
]
checkdepends = ["bash"]
pkgdesc = "Cat clone with wings"
maintainer = "aurelia <git@elia.garden>"
license = "MIT OR Apache-2.0"
url = "https://github.com/sharkdp/bat"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "907554a9eff239f256ee8fe05a922aad84febe4fe10a499def72a4557e9eedfb"


def post_install(self):
    self.install_man("gen/assets/manual/bat.1")
    self.install_license("LICENSE-MIT")
    self.install_completion("gen/assets/completions/bat.bash", "bash")
    self.install_completion("gen/assets/completions/bat.fish", "fish")
    self.install_completion("gen/assets/completions/bat.zsh", "zsh")
