pkgname = "rust-bootstrap"
pkgver = "1.75.0"
pkgrel = 0
# satisfy revdeps
makedepends = ["zlib", "ncurses-libs", "zstd"]
# overlapping files
depends = ["!rust"]
pkgdesc = "Rust programming language bootstrap toolchain"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT OR Apache-2.0"
url = "https://rust-lang.org"
_urlb = "https://repo.chimera-linux.org/distfiles"
source = [
    f"{_urlb}/rustc-{pkgver}-{self.profile().triplet}.tar.xz",
    f"{_urlb}/rust-std-{pkgver}-{self.profile().triplet}.tar.xz",
]
options = ["!strip"]

match self.profile().arch:
    case "aarch64":
        sha256 = [
            "135e7a7e108bcd9cd7ab00fefc3537ef2eb6f758205dc99776b419cea5e9c40e",
            "4ee83d7337cd50f11ed899d44f2a864e262e510f4160aa638b23efcc1d09a921",
        ]
    case "ppc64le":
        sha256 = [
            "e040c205b0736372b5632cfd47b86be05ddafe2f013f69525710d61f30f54a73",
            "99e0d5d8347354ad46c587be545614d124aa1d4817d7bd70ff672ee9305e2cce",
        ]
    case "ppc64":
        sha256 = [
            "f45c66e84f7e717b251bd3931f0cd5a4aee3887653d4e8cc60ca7a141ba29cd1",
            "596acee0939decc4c3597aa0fb97b4b28dd468cecc987a93133f8b2f61768229",
        ]
    case "riscv64":
        sha256 = [
            "c953666114964d1682fbfd5c1e2b581a2185a2917eef43890a4f198533d67080",
            "ce9a816d5544778e7d101df03aff3db6bc11aca858e32872bad646c24c2c717d",
        ]
    case "x86_64":
        sha256 = [
            "b3c273e2cfca8fcc3681e4735c1ec8fe5303a66b865fd94f335bd77927382a85",
            "ef69c3bf8296078c7da7716f57d666837f0f90f0105949299abe6281d6e8ae17",
        ]
    case _:
        broken = f"not yet built for {self.profile().arch}"


def do_install(self):
    for d in self.cwd.iterdir():
        self.do(
            self.chroot_cwd / d.name / "install.sh",
            "--prefix=/usr",
            f"--destdir={self.chroot_destdir}",
            wrksrc=d.name,
        )
    # remove rust copies of llvm tools
    trip = self.profile().triplet
    for f in (self.destdir / f"usr/lib/rustlib/{trip}/bin").glob("rust-ll*"):
        f.unlink()
    # licenses
    self.install_license(f"rustc-{pkgver}-{self.profile().triplet}/LICENSE-MIT")
