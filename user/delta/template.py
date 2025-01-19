pkgname = "delta"
pkgver = "0.18.2"
pkgrel = 2
build_style = "cargo"
prepare_after_patch = True
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = [
    "libgit2-devel",
    "oniguruma-devel",
    "rust-std",
]
checkdepends = ["git"]
pkgdesc = "Syntax-highlighting pager for git, diff, and grep output"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://github.com/dandavison/delta"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "64717c3b3335b44a252b8e99713e080cbf7944308b96252bc175317b10004f02"
# generates completions with host binary
options = ["!cross"]


def post_build(self):
    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"delta.{shell}", "w") as outf:
            self.do(
                f"target/{self.profile().triplet}/release/delta",
                "--generate-completion",
                shell,
                stdout=outf,
            )


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/delta")
    self.install_license("LICENSE")
    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"delta.{shell}", shell)
