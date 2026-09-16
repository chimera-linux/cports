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
    from cbuild.util import cargo

    self.make_build_env["SHELL_COMPLETIONS_DIR"] = cargo.target_path(
        self, "completions"
    )


def install(self):
    from cbuild.util import cargo

    self.install_license("LICENSE-MIT")
    self.install_bin(cargo.target_path(self, "pastel"))
    self.install_completion(
        cargo.target_path(self, "completions/pastel.bash"), "bash"
    )
    self.install_completion(
        cargo.target_path(self, "completions/_pastel"), "zsh"
    )
    self.install_completion(
        cargo.target_path(self, "completions/pastel.fish"), "fish"
    )
    # for some reason the manpages are in completions/ hah
    self.install_man(cargo.target_path(self, "completions/*.1"), glob=True)
