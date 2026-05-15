# Keep in sync with cargo-auditable
pkgname = "cargo-auditable-bootstrap"
pkgver = "0.7.4"
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
sha256 = "4ce3fefc10d704db496c8701d8b2c8623abfbf5af1c673ff607fd1afa6c68052"


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
