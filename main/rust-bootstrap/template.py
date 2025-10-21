pkgname = "rust-bootstrap"
pkgver = "1.89.0"
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
            "b34bccb954ca2e518f04a1c2aef84ac42911ca2e4eb715e43e5a64e9ded7ca21",
            "ee5eedc6362ab92b7203188f96ed2d784beed700ff8740f432538c3e5d285abb",
        ]
    case "loongarch64":
        sha256 = [
            "809d6f9d030f859740ed78d330284346f47538a3ecd0549450c6898f2dbae3d3",
            "e703dbb9daa4e9eff0b1b47903d31963a0385972c824704e50b5333b317e9182",
        ]
    case "ppc64le":
        sha256 = [
            "81d680c7bda50183b43fdd7d3c4130a621a25235a3deca758761eb745ddceab7",
            "99db29eab63fa04781eb780618acdb9337b85d7a818b7e361b714748821cf53e",
        ]
    case "ppc64":
        sha256 = [
            "b21468e8b8454529b41f2937443d3ac81fbbdbceccedd0f8d4338556709c1f7f",
            "e4174d8d05f1b74ad172f3e1c356b410b80091421628d42f01909489187a0a5e",
        ]
    case "ppc":
        sha256 = [
            "ec108c1f1cc7db9bc181f9e7aefb1d6222e8bfe28b2c3c4839764821eec1f803",
            "44aab5420889a76d521300ef6e55fdcf81331caf9fa19706b23c95cca6bdcfec",
        ]
    case "riscv64":
        sha256 = [
            "b410dcc66bcf48dea39c1067d01816098a1c1c2201a05f61dbb30d8f0e09d97c",
            "5e64c9fcd1a8ade90601ade976a715b8b9e31ee340e891d0803a34a849a004de",
        ]
    case "x86_64":
        sha256 = [
            "65e1658b81eac1dfccdd1bcf39c113a7e0d84e854a0f00413f892b8c2ae90a61",
            "329729cc92c7aa47b2edef14606a53df78cf200bce15715426dc92673208d9a3",
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
    # licenses
    self.install_license(f"rustc-{pkgver}-{self.profile().triplet}/LICENSE-MIT")
