pkgname = "bupstash"
pkgver = "0.12.0"
pkgrel = 0
build_style = "cargo"
# we patch Cargo.toml and Cargo.lock
prepare_after_patch = True
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["libsodium-devel"]
pkgdesc = "Tool for encrypted backups"
license = "MIT"
url = "https://bupstash.io"
source = f"https://github.com/andrewchambers/bupstash/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "a2ce4eeb2caa881a778e823cc70d39c2adb0b301f737c55e44a4dd0fbd6a4265"


def post_install(self):
    self.install_license("LICENSE")
