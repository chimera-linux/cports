pkgname = "selene"
pkgver = "0.29.0"
pkgrel = 0
build_style = "cargo"
prepare_after_patch = True
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Lua linter"
license = "MPL-2.0"
url = "https://github.com/Kampfkarren/selene"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "9882007e7b2d16023cd2c69d64d72afbee65dce7c3ab44a1527f5318667ed2a1"

if self.profile().arch == "loongarch64":
    broken = "busted rustix"


def pre_prepare(self):
    # unsafe-libyaml 0.2.5 does not have the fix for
    # https://github.com/dtolnay/unsafe-libyaml/issues/21 yet
    self.do(
        "cargo",
        "update",
        "--package",
        "unsafe-libyaml",
        "--precise",
        "0.2.10",
        allow_network=True,
    )


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/selene")
