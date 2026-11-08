pkgname = "selene"
pkgver = "0.32.0"
pkgrel = 0
build_style = "cargo"
prepare_after_patch = True
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Lua linter"
license = "MPL-2.0"
url = "https://github.com/Kampfkarren/selene"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "cd208a4b3bae38decc9c7bb797c19615caaecf67606b3e593ca60b64d3416cd5"


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
        "0.2.191",
        allow_network=True,
    )


def install(self):
    from cbuild.util import cargo

    self.install_bin(cargo.target_path(self, "selene"))
