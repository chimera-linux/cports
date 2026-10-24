pkgname = "stash"
pkgver = "0.5.3"
pkgrel = 1
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std", "sqlite-devel", "turnstile"]
pkgdesc = "Wayland clipboard manager with persistent history"
license = "MPL-2.0"
url = "https://github.com/notashelf/stash"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "f4d665bc64e94b010b1b784bc1d7590ff6a01105c32c309d34ea2dbce1077685"


def pre_prepare(self):
    # ppc64le: https://github.com/bytecodealliance/rustix/issues/1675
    self.do(
        "cargo",
        "update",
        "--package",
        "rustix",
        "--precise",
        "1.1.5",
        allow_network=True,
    )


def post_install(self):
    self.install_link("usr/bin/stash-copy", "stash")
    self.install_link("usr/bin/stash-paste", "stash")
    self.install_link("usr/bin/wl-copy", "stash")
    self.install_link("usr/bin/wl-paste", "stash")
    self.install_service(self.files_path / "stash.user")
