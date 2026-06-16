pkgname = "riff"
pkgver = "3.6.1"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Diff filter highlighting which line parts have changed"
license = "MIT"
url = "https://github.com/walles/riff"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "d360058f0e51d162235307498485f92dc57518877f5646f00521b97e92957bbe"
# check may be disabled
options = []


if self.profile().arch in ["loongarch64"]:
    # linux-raw-sys ftbfs
    options += ["!check"]


def pre_prepare(self):
    # the version that is in there is busted on loongarch
    self.do(
        "cargo",
        "update",
        "--package",
        "libc",
        "--precise",
        "0.2.170",
        allow_network=True,
    )


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/riff")
    self.install_license("LICENSE")
