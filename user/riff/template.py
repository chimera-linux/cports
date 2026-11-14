pkgname = "riff"
pkgver = "3.7.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Diff filter highlighting which line parts have changed"
license = "MIT"
url = "https://github.com/walles/riff"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "996d3037788c971fde859720557a04b6910e68b887e058df037a868fddad726b"
# check may be disabled
options = []


if self.profile.arch in ["loongarch64"]:
    # linux-raw-sys ftbfs
    options += ["!check"]


def install(self):
    from cbuild.util import cargo

    self.install_bin(cargo.target_path(self, "riff"))
    self.install_license("LICENSE")
