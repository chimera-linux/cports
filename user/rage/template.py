pkgname = "rage"
pkgver = "0.12.1"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Rust implementation of age"
license = "MIT OR Apache-2.0"
url = "https://github.com/str4d/rage"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "3684e7e269a677180db116cb8115b008ea462dbb6f223f6983dd6750a863afaa"


def install(self):
    from cbuild.util import cargo

    self.install_bin(cargo.target_path(self, "rage"))
    self.install_bin(cargo.target_path(self, "rage-keygen"))

    self.install_man(cargo.target_path(self, "manpages/man1/rage.1.gz"))
    self.install_man(cargo.target_path(self, "manpages/man1/rage-keygen.1.gz"))

    self.install_completion(
        cargo.target_path(self, "completions/rage.bash"), "bash"
    )
    self.install_completion(
        cargo.target_path(self, "completions/rage-keygen.bash"),
        "bash",
        "rage-keygen",
    )

    self.install_completion(cargo.target_path(self, "completions/_rage"), "zsh")
    self.install_completion(
        cargo.target_path(self, "completions/_rage-keygen"),
        "zsh",
        "rage-keygen",
    )

    self.install_completion(
        cargo.target_path(self, "completions/rage.fish"), "fish"
    )
    self.install_completion(
        cargo.target_path(self, "completions/rage-keygen.fish"),
        "fish",
        "rage-keygen",
    )

    self.install_license("LICENSE-APACHE")
    self.install_license("LICENSE-MIT")
