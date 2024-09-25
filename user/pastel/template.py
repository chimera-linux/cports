pkgname = "pastel"
pkgver = "0.10.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "CLI tool to generate, analyze, convert and manipulate colors"
maintainer = "ttyyls <contact@behri.org>"
license = "Apache-2.0 OR MIT"
url = "https://github.com/sharkdp/pastel"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "7848cd6d2ad8db6543b609dece7c9c28b4720c09fb13aeb204dd03d152159dd2"


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
