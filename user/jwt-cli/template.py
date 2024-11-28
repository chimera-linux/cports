pkgname = "jwt-cli"
pkgver = "6.2.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "CLI tool to decode and encode JWTs"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://github.com/mike-engel/jwt-cli"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "49d67d920391978684dc32b75e553a2abbd46c775365c0fb4b232d22c0ed653a"
# generates completions with host binary
options = ["!cross"]


def post_build(self):
    for shell in ["bash", "fish", "zsh", "nushell"]:
        with open(self.cwd / f"jwt.{shell}", "w") as outf:
            self.do(
                f"target/{self.profile().triplet}/release/jwt",
                "completion",
                shell,
                stdout=outf,
            )


def post_install(self):
    self.install_license("LICENSE.md")
    for shell in ["bash", "fish", "zsh", "nushell"]:
        self.install_completion(f"jwt.{shell}", shell, "jwt")
