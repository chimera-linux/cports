pkgname = "riff"
pkgver = "3.6.2"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Diff filter highlighting which line parts have changed"
license = "MIT"
url = "https://github.com/walles/riff"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "2d84d005f33444143eb8f68eb72024cd7eb9addd0b933665aaf44de7e071c175"
# check may be disabled
options = []


if self.profile.arch in ["loongarch64"]:
    # linux-raw-sys ftbfs
    options += ["!check"]


def install(self):
    from cbuild.util import cargo

    self.install_bin(cargo.target_path(self, "riff"))
    self.install_license("LICENSE")
