pkgname = "emmylua-analyzer-rust"
pkgver = "0.25.1"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "openssl3-devel", "pkgconf"]
makedepends = ["rust-std"]
pkgdesc = "Lua language server, formatter, linter, and doc generator"
license = "MIT"
url = "https://github.com/EmmyLuaLs/emmylua-analyzer-rust"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "497b80cf970afbcced36d446a29bde2b59a86f10bbfa936d86f048450553fb0c"
# check may be disabled
options = []

if self.profile().wordsize == 32:
    broken = "uses atomic64"

if self.profile().arch in ["ppc64le"]:
    # stack overflow in several tests
    options += ["!check"]


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/emmylua_ls")
    self.install_bin(f"target/{self.profile().triplet}/release/luafmt")
    self.install_bin(f"target/{self.profile().triplet}/release/emmylua_check")
    self.install_bin(f"target/{self.profile().triplet}/release/emmylua_doc_cli")
    self.install_bin(
        f"target/{self.profile().triplet}/release/schema_to_emmylua"
    )
    self.install_license("LICENSE")
