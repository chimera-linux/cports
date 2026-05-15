pkgname = "onefetch"
pkgver = "2.27.1"
pkgrel = 0
build_style = "cargo"
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
sha256 = "3a6f82d3da4da62b2e5406bbe307b0afc73cd8fcc4855534886d80ea0121cc03"
# cross: generates completions with host binary
options = ["!cross"]


def post_patch(self):
    from cbuild.util import cargo

    cargo.clear_vendor_checksums(self, "gix-index-0.48.0")


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
