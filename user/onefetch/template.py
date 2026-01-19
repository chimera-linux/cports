pkgname = "onefetch"
pkgver = "2.26.1"
pkgrel = 0
build_style = "cargo"
prepare_after_patch = True
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = [
    "rust-std",
    "zlib-ng-compat-devel",
    "zstd-devel",
]
checkdepends = ["bash", "git"]
pkgdesc = "Displays project information and code statistics"
license = "MIT"
url = "https://onefetch.dev"
source = f"https://github.com/o2sh/onefetch/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "ff43255d7c138c448cfdd1abacb01c6abe0c3e3886024e98ff077b28d4dc0ddc"
# cross: generates completions with host binary
options = ["!cross"]


def post_build(self):
    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"onefetch.{shell}", "w") as outf:
            self.do(
                f"target/{self.profile().triplet}/release/onefetch",
                "--generate",
                shell,
                stdout=outf,
            )


def install(self):
    self.install_license("LICENSE.md")
    self.install_bin(f"target/{self.profile().triplet}/release/onefetch")
    self.install_man("docs/onefetch.1")
    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"onefetch.{shell}", shell)
