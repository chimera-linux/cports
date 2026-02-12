pkgname = "rust-bootstrap"
pkgver = "1.92.0"
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
            "2e9f12e49c9c2f00eabeb268077393c578674c274362046d09b39c784fb71511",
            "c7bdf73ceadef99c18c5ef07c14047026d15fad9bd01b21222c6ac32745df8df",
        ]
    case "loongarch64":
        sha256 = [
            "47a0a0659e860ecfc0aa6d0ddc115c52ed8327fdc9b2120ab846e0842249a3ed",
            "838c3cd7955367bfe6b809f207c94baa54e590f40055a26f6dda9f3fbdf7da8d",
        ]
    case "ppc64le":
        sha256 = [
            "d758bff94374f31fe9c3e0e67e760ac36c37b9cc384a089da2ecf59dfcc804ef",
            "102fb780ff10f31fe53febf5262fc262841fffa3501302cbd639831e663a53a8",
        ]
    case "ppc64":
        sha256 = [
            "11dc0440df2aaefeeb32d7558aeeaa47bd7fc596f350864c66e03cf3121be026",
            "0cc156a4afedfd5ac4db0fc450532f157d5d6140c8739482eaf2b295bd3109aa",
        ]
    case "ppc":
        sha256 = [
            "bae4d351550e3a20269a79968668918f423a79c3fc0488f90e8757e0c5713b78",
            "adf29539d21dc1163cdc784c9ae3daf172b555dc6bb8498c49fabf37563c6f5a",
        ]
    case "riscv64":
        sha256 = [
            "f0b6c48217e674bc82a8e8f5f4396b6a32f9fd7c534d2ccc7e73c55e0cbd65bb",
            "679d2991696b2c951bc3625965d4158daaf0c1dc13b8468e67818df2f64709ce",
        ]
    case "x86_64":
        sha256 = [
            "0b6b0b64859b3dffa47a2e75ce7487d5f77aad75cb224f4e958c57975d123f1b",
            "c6afa9db6166e198cad9e178fe9bf5244969efb704bae5c38e00b583e7f0d92e",
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
