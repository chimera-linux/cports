pkgname = "jwt-cli"
pkgver = "6.1.1"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "CLI tool to decode and encode JWTs"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://github.com/mike-engel/jwt-cli"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "80193ea16f603b65fccb31c6da383ca531d23c0e171f443761958bed5e973e1d"
# generates completions with host binary
options = ["!cross"]


def post_build(self):
    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"jwt.{shell}", "w") as outf:
            self.do(
                f"target/{self.profile().triplet}/release/jwt",
                "completion",
                shell,
                stdout=outf,
            )


def post_install(self):
    self.install_license("LICENSE.md")
    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"jwt.{shell}", shell, "jwt")
