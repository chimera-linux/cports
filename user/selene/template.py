pkgname = "selene"
pkgver = "0.30.1"
pkgrel = 0
build_style = "cargo"
prepare_after_patch = True
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Lua linter"
license = "MPL-2.0"
url = "https://github.com/Kampfkarren/selene"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "61c66d7e40d8d00fe8364a2696c7f87bcb976d838bd681fd802d427c7675a872"


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
    # rustix loongarch64
    self.do(
        "cargo",
        "update",
        "--package",
        "libc",
        "--precise",
        "0.2.174",
        allow_network=True,
    )


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/selene")
