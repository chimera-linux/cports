pkgname = "emmylua-analyzer-rust"
pkgver = "0.25.1"
pkgrel = 0
build_style = "cargo"
make_check_args = [
    "--",
    # ppc64le stack overflow
    "--skip=compilation::analyzer::flow::bind_analyze::engine::tests::test_flow_bind_deep_logical_chain",
]

hostmakedepends = ["cargo-auditable", "openssl3-devel", "pkgconf"]
makedepends = ["rust-std"]
pkgdesc = "Lua language server, formatter, linter, and doc generator"
license = "MIT"
url = "https://github.com/EmmyLuaLs/emmylua-analyzer-rust"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "497b80cf970afbcced36d446a29bde2b59a86f10bbfa936d86f048450553fb0c"

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
