# Keep in sync with cargo-auditable
pkgname = "cargo-auditable-bootstrap"
pkgver = "0.7.2"
pkgrel = 0
build_style = "cargo"
make_build_args = ["-p", "cargo-auditable"]
make_check_args = [
    *make_build_args,
    "--",
    "--skip=test_wasm",
]
hostmakedepends = ["cargo"]
makedepends = ["rust-std", "rust-wasm"]
depends = ["cargo"]
pkgdesc = "Tool for embedding dependency information in rust binaries"
license = "Apache-2.0 OR MIT"
url = "https://github.com/rust-secure-code/cargo-auditable"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "61d780d55dc35e4ab9c9b6dce744a35a03754c128b3a95aeb76f83c397807fbd"


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
    self.install_bin(
        f"./target/{self.profile().triplet}/release/cargo-auditable"
    )
    self.install_license("LICENSE-MIT")
