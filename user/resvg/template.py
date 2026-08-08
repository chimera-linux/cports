pkgname = "resvg"
pkgver = "0.48.1"
pkgrel = 0
build_style = "cargo"
make_check_args = ["--workspace", "--exclude=resvg-capi"]
hostmakedepends = ["cargo-auditable", "cargo-c", "pkgconf"]
makedepends = ["rust-std"]
pkgdesc = "SVG rendering library"
license = "Apache-2.0 OR MIT"
url = "https://github.com/linebender/resvg"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "40dafea6b4b9d01e9d28b6d49f1e912daf3e9055676ad9179a5a2db6e7386945"


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
