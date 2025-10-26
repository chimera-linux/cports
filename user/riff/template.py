pkgname = "riff"
pkgver = "3.5.1"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Diff filter highlighting which line parts have changed"
license = "MIT"
url = "https://github.com/walles/riff"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "0f7a023e3fc0fad8822aa94e52d0c70ece5f0bf1ed4b4fa56d5f12d739bd82d4"
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
