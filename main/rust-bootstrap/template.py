pkgname = "rust-bootstrap"
pkgver = "1.97.1"
pkgrel = 0
# satisfy revdeps
makedepends = ["zlib-ng-compat", "ncurses-libs", "zstd"]
# overlapping files
depends = ["!rust"]
pkgdesc = "Rust programming language bootstrap toolchain"
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
            "15ec31bbe0694ab27e249aed561206a7e31144d7b98ba84175c5c69696aff473",
            "f87616712a3fd7c562682d377be50c6e838c73876c128069b90898ecc0a7c055",
        ]
    case "loongarch64":
        sha256 = [
            "413ec6e70f030a7a9863843b54c889eb256c981375e3da8e382a02eb9cd65956",
            "2097a7ac6212fdf843d94bc4aba25811bbe154ec13a1a24a009d6a45c82c08e9",
        ]
    case "ppc64le":
        sha256 = [
            "d7f3f59dccb9ed15106359987c2c0e8249f172d82b5f2eaf7a315921e596717f",
            "d58717459413cc4e54d02c7a6aa692c304bcabe62ae06447518ff1c6ae4d0cbf",
        ]
    case "riscv64":
        sha256 = [
            "2cd33f31c80d9afc218354880e0702d9fac0c15ef4d20fd9458715acfc484d71",
            "a3167a791e289b16b8bbee52d6311abb06b68516e9215b58ecf2a9ad07b133d7",
        ]
    case "x86_64":
        sha256 = [
            "0d02f471281bdb3617616bd151d97779731ec6b53932328455d8c91860524c45",
            "7476a7f7c24efa02b9b2d80ba568b1466ed364d94eddf8a3d542943e3134d610",
        ]
    case _:
        broken = f"not yet built for {self.profile().arch}"


def install(self):
    for d in self.cwd.iterdir():
        self.do(
            self.chroot_cwd / d.name / "install.sh",
            "--prefix=/usr",
            f"--destdir={self.chroot_destdir}",
            wrksrc=d.name,
        )
    # remove rust copies of llvm tools
    trip = self.profile().triplet
    self.uninstall(f"usr/lib/rustlib/{trip}/bin")
    # whatever
    self.uninstall("usr/etc")
    # licenses
    self.install_license(f"rustc-{pkgver}-{self.profile().triplet}/LICENSE-MIT")
