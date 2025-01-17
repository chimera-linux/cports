pkgname = "berg"
pkgver = "0.4.7"
pkgrel = 0
build_style = "cargo"
prepare_after_patch = True
hostmakedepends = [
    "cargo-auditable",
    "pkgconf",
]
makedepends = [
    "rust-std",
    "openssl-devel",
    "libgit2-devel",
]
pkgdesc = "CLI Tool for forgejo"
maintainer = "ttyyls <contact@behri.org>"
license = "AGPL-3.0-or-later"
url = "https://codeberg.org/Aviac/codeberg-cli"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "a8d1356faab84076f14977652dabbfcad4411f49beb4d11a1bc0ee8936bd1d6c"
# check: only one defined test (skipped)
# cross: generates completions with host binary
options = ["!check", "!cross"]


def post_build(self):
    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"berg.{shell}", "w") as outf:
            self.do(
                f"target/{self.profile().triplet}/release/berg",
                "completion",
                shell,
                stdout=outf,
            )


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/berg")
    self.install_license("LICENSE")
    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"berg.{shell}", shell)
