pkgname = "emmylua-analyzer-rust"
pkgver = "0.25.1"
pkgrel = 1
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

if self.profile().arch in ["loongarch64", "ppc64le"]:
    # loongarch64: some tests time out
    # ppc64le: stack overflow in several tests
    options += ["!check"]


def install(self):
    self.cargo.install(wrksrc="crates/emmylua_ls")
    self.cargo.install(wrksrc="crates/emmylua_formatter")
    self.cargo.install(wrksrc="crates/emmylua_check")
    self.cargo.install(wrksrc="crates/emmylua_doc_cli")
    self.cargo.install(wrksrc="crates/schema_to_emmylua")


def post_install(self):
    self.install_license("LICENSE")
