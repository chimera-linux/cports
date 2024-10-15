pkgname = "bupstash"
pkgver = "0.12.0"
pkgrel = 0
build_style = "cargo"
make_build_args = []
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["libsodium-devel"]
pkgdesc = "Bupstash is a tool for encrypted backups"
maintainer = "tj <tjheeta@gmail.com>"
license = "MIT"
url = "https://github.com/andrewchambers/bupstash"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "a2ce4eeb2caa881a778e823cc70d39c2adb0b301f737c55e44a4dd0fbd6a4265"

def post_patch(self):
    from cbuild.util import cargo

    # Adjust bupstash dependencies for musl changes of -D_LARGEFILE_SOURCE / -D_LARGEFILE64_SOURCE
    cargo.clear_vendor_checksums(self, "nix")
    cargo.clear_vendor_checksums(self, "getrandom")

def post_install(self):
    self.install_license("LICENSE")
