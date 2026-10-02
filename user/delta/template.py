pkgname = "delta"
pkgver = "0.20.1"
pkgrel = 0
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
license = "MIT"
url = "https://github.com/dandavison/delta"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "d9d502396e3595ee8fd926f1ed2e54ac9935baabd3569a3753efab36304f90fa"
# generates completions with host binary
options = ["!cross"]


def post_build(self):
    from cbuild.util import cargo

    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"delta.{shell}", "w") as outf:
            self.do(
                cargo.target_path(self, "delta"),
                "--generate-completion",
                shell,
                stdout=outf,
            )


def install(self):
    from cbuild.util import cargo

    self.install_bin(cargo.target_path(self, "delta"))
    self.install_license("LICENSE")
    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"delta.{shell}", shell)
