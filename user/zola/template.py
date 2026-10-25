pkgname = "zola"
pkgver = "0.23.6"
pkgrel = 0
build_style = "cargo"
prepare_after_patch = True
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["rust-std", "openssl3-devel", "oniguruma-devel", "zstd-devel"]
pkgdesc = "Static site generator"
license = "MIT"
url = "https://www.getzola.org"
source = f"https://github.com/getzola/zola/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "193db594222cd9c1097387ce17272cbbe672c3a894c263f6f4c436a7fedb379f"
# generates completions with host bins
options = ["!cross"]

if self.profile.wordsize == 32:
    broken = "runs out of memory during linking"


def post_build(self):
    from cbuild.util import cargo

    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"zola.{shell}", "w") as outf:
            self.do(
                cargo.target_path(self, "zola"),
                "completion",
                shell,
                stdout=outf,
            )


def install(self):
    from cbuild.util import cargo

    self.install_bin(cargo.target_path(self, "zola"))
    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"zola.{shell}", shell)
    self.install_license("LICENSE")
