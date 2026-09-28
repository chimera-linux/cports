pkgname = "typstyle"
pkgver = "0.15.1"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Typst code formatter"
license = "Apache-2.0"
url = "https://github.com/Enter-tainer/typstyle"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "0f1b86584a0eb93b0cef374ddcc62508c46ee76cd8b5ede31414260d29a38f12"

if self.profile.wordsize == 32:
    broken = "needs atomic64"

if self.profile.arch in ["loongarch64"]:
    broken = "sigbus in tests"


def install(self):
    from cbuild.util import cargo

    self.install_bin(cargo.target_path(self, "typstyle"))
