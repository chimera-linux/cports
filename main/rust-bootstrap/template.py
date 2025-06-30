pkgname = "rust-bootstrap"
pkgver = "1.87.0"
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
            "448b1cad8d03a8043209fa36ce2d5e2a4cc89a4937095c1f31ce1930cf74d317",
            "021525c8b7f2da8cd3962d53524dd2d334a8554473f6d98f2633c16942f75ec2",
        ]
    case "loongarch64":
        sha256 = [
            "dea393ab19d4ccf916f5b7d7482b94262ce200035438813f9a26e121dad46c6f",
            "ad0a44126c903905fdcd0c66c179d1cf86afbbe966095f5f0b5b8ce7656d3250",
        ]
    case "ppc64le":
        sha256 = [
            "e11fbef6d8f4b114c75ec401e58cb070aa24683405643f1d632251b922fa9454",
            "4e142e3d1b0b6c2e901786926ed70fc8c3e45b34a35f02751cba8bf869743020",
        ]
    case "ppc64":
        sha256 = [
            "e823ee54cbd2c04a32190fd67a9616c16ebf36c2850471d5c84b818d187afa17",
            "a481841d33393bec331c7fd40e6cb58f910080af503174645e8f6964bea68455",
        ]
    case "ppc":
        sha256 = [
            "ec4b9bcaa040669dd3a5143347a5973888b77579609e33f21c3032a618fab35b",
            "fa9c81e91502a6abd3393f72de6e550c8da1598167c9880f318c330036ca4f94",
        ]
    case "riscv64":
        sha256 = [
            "8177f8dce65535e9b02d5eb257ccfde38a02e01847c5d119b5dcffe54ef46d1f",
            "89399c036d3b8240cef7fe345676e3acff67adc800add9c2c7365bd7cefcd98c",
        ]
    case "x86_64":
        sha256 = [
            "b3e9bec8490db1d68ef89fe4cbed1a1091258e858adf3d8e5179701466c6d7d9",
            "302543344788285de4e7afda3831fd484f84387fef3bbb2c4b4bdd0fb2c73159",
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
