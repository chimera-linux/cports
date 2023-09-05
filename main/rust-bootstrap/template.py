pkgname = "rust-bootstrap"
pkgver = "1.71.0"
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
            "c0632d1164a8570bf55d6157f8bd53df68284553dba7875dd75b93212aadf2ff",
            "05d2610eac03ef2cabc24b9fe7d7ad905f6c3835d74276abbbccaa9b333887f2",
        ]
    case "ppc64le":
        sha256 = [
            "9b498bb08810f77fcd8ed2313fb085963f49829aa74d2b40c3ee5c6daa0cf6f1",
            "7faf383a01009baa649dd6998f01efd5ed106b8067ba69934df5370ddf9d8dcc",
        ]
    case "ppc64":
        sha256 = [
            "3f0e052357c1a9a92bea414a6e524e5e1a6c29e4e8d41a92445b7013c55a0954",
            "95e80d0fde060dc2d70447e992cfeaa5b9762491e08ef8f199477ce033b83bf5",
        ]
    case "riscv64":
        sha256 = [
            "bf46411310f71ca2dff8aa3e418ee860a219da461a0e019980661b120c26f4bf",
            "ae935085a83be4c180e3da90caf27f6720d981e02b0473f0589f3e38795700d8",
        ]
    case "x86_64":
        sha256 = [
            "dad44f0009c01f2460367cc661cb249cbeaadaf2e0501004b0cb170a74beb503",
            "6531edb8e295b0e7bf790949db4277072f5fa324e229de8f44f33a5af062ac54",
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
