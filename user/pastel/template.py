pkgname = "pastel"
pkgver = "0.12.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
depends = ["zenity"]
pkgdesc = "CLI tool to generate, analyze, convert and manipulate colors"
license = "Apache-2.0 OR MIT"
url = "https://github.com/sharkdp/pastel"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "2903853f24d742fe955edd9bea17947eb8f3f44000a8ac528d16f2ea1e52b78b"


def init_build(self):
    self.make_build_env = {
        "SHELL_COMPLETIONS_DIR": f"target/{self.profile().triplet}/release/completions"
    }


def install(self):
    self.install_license("LICENSE-MIT")
    with self.pushd(f"target/{self.profile().triplet}/release"):
        self.install_bin("pastel")
        self.install_completion("completions/pastel.bash", "bash")
        self.install_completion("completions/_pastel", "zsh")
        self.install_completion("completions/pastel.fish", "fish")
        # for some reason the manpages are in completions/ hah
        self.install_man("completions/*.1", glob=True)
