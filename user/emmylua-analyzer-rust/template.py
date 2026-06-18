pkgname = "emmylua-analyzer-rust"
pkgver = "0.23.2"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "openssl3-devel", "pkgconf"]
makedepends = ["rust-std"]
pkgdesc = "Lua language server, formatter, linter, and doc generator"
license = "MIT"
url = "https://github.com/EmmyLuaLs/emmylua-analyzer-rust"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "6c4d380dd34ee3600684f4bfd35d7fd98d2c77334a3b4a6ad46ea5af106f667b"

if self.profile().wordsize == 32:
    broken = "uses atomic64"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/emmylua_ls")
    self.install_bin(f"target/{self.profile().triplet}/release/luafmt")
    self.install_bin(f"target/{self.profile().triplet}/release/emmylua_check")
    self.install_bin(f"target/{self.profile().triplet}/release/emmylua_doc_cli")
    self.install_bin(
        f"target/{self.profile().triplet}/release/schema_to_emmylua"
    )
    self.install_license("LICENSE")
