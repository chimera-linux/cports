pkgname = "resvg"
pkgver = "0.50.0"
pkgrel = 0
build_style = "cargo"
make_check_args = ["--workspace", "--exclude=resvg-capi"]
hostmakedepends = ["cargo-auditable", "cargo-c", "pkgconf"]
makedepends = ["rust-std"]
pkgdesc = "SVG rendering library"
license = "Apache-2.0 OR MIT"
url = "https://github.com/linebender/resvg"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "ea6629ecaf8ae523aaa42b23217db7fdbed5d4bb070a2574af0d01040195beb1"


def build(self):
    self.cargo.build(["--workspace", "--exclude=resvg-capi"])
    self.cargo.cbuild(["--manifest-path", "crates/c-api/Cargo.toml"])


def install(self):
    from cbuild.util import cargo

    self.install_bin(cargo.target_path(self, "resvg"))
    self.install_bin(cargo.target_path(self, "usvg"))
    self.cargo.cinstall(args=["--manifest-path", "crates/c-api/Cargo.toml"])
    self.install_license("LICENSE-MIT")


@subpackage("resvg-progs")
def _(self):
    self.subdesc = "CLI"

    return self.default_progs()


@subpackage("resvg-devel")
def _(self):
    return self.default_devel()
