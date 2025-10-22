pkgname = "bat"
pkgver = "0.26.0"
pkgrel = 0
build_style = "cargo"
prepare_after_patch = True
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = [
    "libgit2-devel",
    "oniguruma-devel",
    "rust-std",
    "zlib-ng-compat-devel",
]
checkdepends = ["bash"]
pkgdesc = "Cat clone but larger"
license = "MIT OR Apache-2.0"
url = "https://github.com/sharkdp/bat"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "ccf3e2b9374792f88797a28ce82451faeae0136037cb8c8b56ba0a6c1a94fd69"


def init_build(self):
    self.make_build_env["BAT_ASSETS_GEN_DIR"] = f"{self.chroot_cwd}/gen"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/bat")
    self.install_man("gen/assets/manual/bat.1")
    self.install_license("LICENSE-MIT")
    self.install_completion("gen/assets/completions/bat.bash", "bash")
    self.install_completion("gen/assets/completions/bat.fish", "fish")
    self.install_completion("gen/assets/completions/bat.zsh", "zsh")
