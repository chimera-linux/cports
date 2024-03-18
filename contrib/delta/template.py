pkgname = "delta"
pkgver = "0.17.0"
pkgrel = 1
build_style = "cargo"
hostmakedepends = ["cargo", "pkgconf"]
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
sha256 = "1abd21587bcc1f2ef0cd342784ce990da9978bc345578e45506419e0952de714"
# generates completions with host binary
options = ["!cross"]


def do_prepare(self):
    # we patch the lockfile so vendor after patch
    pass


def post_patch(self):
    from cbuild.util import cargo

    self.cargo.vendor()
    cargo.setup_vendor(self)


def post_build(self):
    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"delta.{shell}", "w") as outf:
            self.do(
                f"target/{self.profile().triplet}/release/delta",
                "--generate-completion",
                shell,
                stdout=outf,
            )


def post_install(self):
    self.install_license("LICENSE")
    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"delta.{shell}", shell)
