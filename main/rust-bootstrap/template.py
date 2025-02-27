pkgname = "rust-bootstrap"
pkgver = "1.84.1"
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
            "14f6159c1ef688b923048c809964df27dd72be9c8e5982106f9d880228f1a353",
            "3533f27a9bdd4b21664065dd73f2bee67d4ed33c83c5b94b55c9ac9420bdd20d",
        ]
    case "ppc64le":
        sha256 = [
            "6f1474b99b6e52d704fba070b9096b2c7120e409b2b5570bf0efb58df9aba410",
            "24708e63b3ea6a6f98428316831d3b78f6d6389c14d87fbd1acee96361b5bbcf",
        ]
    case "ppc64":
        sha256 = [
            "e00fbc1c9ce796c34525a17975b85553ccc25ab27ffeb27bf9825e851053a316",
            "c87f5732d202551987ecd07188ff50b3d4c5d9faac65ede74cdf44b4ddfef7fd",
        ]
    case "ppc":
        sha256 = [
            "592e688440fd7077470f6a3f799a284ba57c0a550082e272c0cec77eddc8fe14",
            "7a6bf89844fd9058461d6f08b21573f6d6b72b0cdd193ce1799d8ffef677ea62",
        ]
    case "riscv64":
        sha256 = [
            "d6a830f8ee7cf1ecec66a724dd67c5de3bd9d60d4414f6f2e84fe91d33d83bbc",
            "2f50e6acaf56af00442c533bd0544c924c79bd75a26be26dfbfbdcfcc24ddf2f",
        ]
    case "x86_64":
        sha256 = [
            "944b80b9a87b592478b10a8b9643346f742681df378adf7f0ce849dd76eeb025",
            "721efc512a2b16cdfb4e4bebb7b9312207ed585946f12467fdda210ba0a8ef69",
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
    for f in (self.destdir / f"usr/lib/rustlib/{trip}/bin").glob("rust-ll*"):
        f.unlink()
    # licenses
    self.install_license(f"rustc-{pkgver}-{self.profile().triplet}/LICENSE-MIT")
