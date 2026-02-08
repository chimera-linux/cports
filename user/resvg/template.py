pkgname = "resvg"
pkgver = "0.47.0"
pkgrel = 0
build_style = "cargo"
make_check_args = ["--workspace", "--exclude=resvg-capi"]
hostmakedepends = ["cargo-auditable", "cargo-c", "pkgconf"]
makedepends = ["rust-std"]
pkgdesc = "SVG rendering library"
license = "Apache-2.0 OR MIT"
url = "https://github.com/linebender/resvg"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "7869119fd822983b0a0bc2469bc94d59e7908fc12165fa67a105a4fa25087f9a"


def build(self):
    self.cargo.build(["--workspace", "--exclude=resvg-capi"])
    self.cargo.cbuild(["--manifest-path", "crates/c-api/Cargo.toml"])


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/resvg")
    self.install_bin(f"target/{self.profile().triplet}/release/usvg")
    self.cargo.cinstall(args=["--manifest-path", "crates/c-api/Cargo.toml"])
    self.install_license("LICENSE-MIT")


@subpackage("resvg-progs")
def _(self):
    self.subdesc = "CLI"

    return self.default_progs()


@subpackage("resvg-devel")
def _(self):
    return self.default_devel()
