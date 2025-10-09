pkgname = "riff"
pkgver = "3.4.1"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Diff filter highlighting which line parts have changed"
license = "MIT"
url = "https://github.com/walles/riff"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "d209e5b5a68907382cc91061d2e0570789293214b402c1b344008760fe298302"
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


def post_install(self):
    self.install_license("LICENSE")
