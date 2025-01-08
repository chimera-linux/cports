pkgname = "bat"
pkgver = "0.25.0"
pkgrel = 0
build_style = "cargo"
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
sha256 = "4433403785ebb61d1e5d4940a8196d020019ce11a6f7d4553ea1d324331d8924"


def init_build(self):
    self.make_build_env["BAT_ASSETS_GEN_DIR"] = f"{self.chroot_cwd}/gen"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/bat")
    self.install_man("gen/assets/manual/bat.1")
    self.install_license("LICENSE-MIT")
    self.install_completion("gen/assets/completions/bat.bash", "bash")
    self.install_completion("gen/assets/completions/bat.fish", "fish")
    self.install_completion("gen/assets/completions/bat.zsh", "zsh")
