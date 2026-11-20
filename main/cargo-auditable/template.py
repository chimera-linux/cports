# Keep in sync with cargo-auditable-bootstrap
pkgname = "cargo-auditable"
pkgver = "0.7.7"
pkgrel = 0
build_style = "cargo"
make_build_args = ["-p", "cargo-auditable"]
make_check_args = [
    *make_build_args,
    "--",
    "--skip=test_wasm",
]
hostmakedepends = ["cargo-auditable-bootstrap"]
makedepends = ["rust-std", "rust-wasm"]
depends = ["cargo"]
pkgdesc = "Tool for embedding dependency information in rust binaries"
license = "Apache-2.0 OR MIT"
url = "https://github.com/rust-secure-code/cargo-auditable"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "cab2a4b65cfde0734c98416740d24d4e3f03441ea8a0b385f0431e35244a05aa"


def pre_prepare(self):
    vendor_dir = self.chroot_srcdir / "vendor"
    for lockfile in self.find("", "Cargo.lock"):
        if len(lockfile.parents) == 1 or str(lockfile.parents[-2]) == "vendor":
            continue

        self.cargo.invoke(
            "vendor",
            args=[vendor_dir],
            wrksrc=lockfile.parent,
            offline=False,
        )


def install(self):
    from cbuild.util import cargo

    self.install_bin(cargo.target_path(self, "cargo-auditable"))
    self.install_license("LICENSE-MIT")
