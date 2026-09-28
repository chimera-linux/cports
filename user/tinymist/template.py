pkgname = "tinymist"
pkgver = "0.15.8"
pkgrel = 0
build_style = "cargo"
make_build_args = ["--features=cli", "--bin", "tinymist", "--bin", "typlite"]
make_build_env = {"VERGEN_GIT_DESCRIBE": pkgver}
hostmakedepends = ["cargo", "pkgconf"]
makedepends = ["rust-std", "openssl3-devel"]
depends = ["typst"]
pkgdesc = "Language server for Typst"
license = "Apache-2.0"
url = "https://myriad-dreamin.github.io/tinymist"
source = f"https://github.com/Myriad-Dreamin/tinymist/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "46cab76c48dc27cefd5ea8160484ebc2ad5c428d5fddb65681d35cb55662fd90"
# check: takes forever
options = ["!check", "!cross"]

if self.profile.wordsize == 32:
    broken = "needs atomic64"


def post_build(self):
    from cbuild.util import cargo

    for shell in ["bash", "fish", "zsh", "nushell"]:
        with open(self.cwd / f"tinymist.{shell}", "w") as f:
            self.do(
                cargo.target_path(self, "tinymist"),
                "completion",
                shell,
                stdout=f,
            )


def install(self):
    from cbuild.util import cargo

    for shell in ["bash", "fish", "zsh", "nushell"]:
        self.install_completion(f"tinymist.{shell}", shell)
    self.install_bin(cargo.target_path(self, "tinymist"))
    self.install_bin(cargo.target_path(self, "typlite"))
