pkgname = "selene"
pkgver = "0.28.0"
pkgrel = 1
build_style = "cargo"
prepare_after_patch = True
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Lua linter"
license = "MPL-2.0"
url = "https://github.com/Kampfkarren/selene"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "c51acf52e7c3136cd0b67b9a39a4a447c8f0257371b2b2acc7e77587260a377b"


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
