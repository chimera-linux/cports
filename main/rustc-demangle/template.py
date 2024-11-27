pkgname = "rustc-demangle"
pkgver = "0.1.24"
pkgrel = 0
build_style = "cargo"
make_build_args = ["--workspace"]
make_check_args = [*make_build_args]
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Library and tool to demangle Rust symbols"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "Apache-2.0 OR MIT"
url = "https://github.com/rust-lang/rustc-demangle"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "0a130040b74af0f1764b82fa55a8510d7d9284847206c32037f5660596060888"


def install(self):
    self.install_bin(
        f"target/{self.profile().triplet}/release/demangle",
        name="rust-demangle",
    )
    self.install_lib(
        f"target/{self.profile().triplet}/release/librustc_demangle.so"
    )
    self.install_lib(
        f"target/{self.profile().triplet}/release/librustc_demangle.a"
    )
    self.install_files("crates/capi/include", "usr")
    self.install_license("LICENSE-MIT")


@subpackage("rustc-demangle-libs")
def _(self):
    self.subdesc = "runtime library"
    # library without soname/version
    return ["usr/lib/librustc_demangle.so"]


@subpackage("rustc-demangle-devel")
def _(self):
    self.depends += [self.with_pkgver("rustc-demangle-libs")]
    return self.default_devel()
