pkgname = "pastel"
pkgver = "0.11.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
depends = ["zenity"]
pkgdesc = "CLI tool to generate, analyze, convert and manipulate colors"
license = "Apache-2.0 OR MIT"
url = "https://github.com/sharkdp/pastel"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "98639ae6539da5a4c20993daa559ca2d19dde63b601bcb29bb0cebbf56b1ac08"


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
