pkgname = "rust-bootstrap"
pkgver = "1.90.0"
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
            "40944a144ecce8a70919623ac25c19b2ef4da3a59349d65ae8ef32dc39e77c1c",
            "6875a53259f6d79c63fe4a90b073e6a296d70dea22460737ef7f901f22419496",
        ]
    case "loongarch64":
        sha256 = [
            "5ea8c79a0f3c3560a1d53ead275e174ca66d473e13ce962011bdf9bec7ff2e02",
            "2c5aae092ffb4c1f018410e30d13f0618c2137eb7091067448bef02fb9a1267d",
        ]
    case "ppc64le":
        sha256 = [
            "a754f90fdfd0c7e2da1a6ee52b9b54ad557362017a1d18590a94eccd54587b62",
            "112cc980691915ff49162e23966a7a820aedb903e558b64caa78490ec99510a9",
        ]
    case "ppc64":
        sha256 = [
            "05b6a0b32042b6e261a5f84dbfddbc521a1baf9a19c32e26a61b1f8cffcb4164",
            "402417e6f54fd8aa508db1f07b555b3cbe79f5097d901c88021325d1a90b1365",
        ]
    case "ppc":
        sha256 = [
            "8deb6f91e847a495c2b5ee5bb02afae0ff210a753848a5ad7e7bf65ad50274bc",
            "3cadb58d448a4b26da94529cbc3e7cbd73e605144ff5b2bf0e2dbe3a99686e52",
        ]
    case "riscv64":
        sha256 = [
            "72f6902372c809ee6564f252278678c3d8393ef3abe578a7fd10bf9182fd8aea",
            "a432728db74eead923069bb9f934756f526470813e21a60822263c2d916f8d95",
        ]
    case "x86_64":
        sha256 = [
            "9dadc11718f9d4c638ed5ebebee2b505699476b15b1e1f260446d169abba4bca",
            "1533e9980331933c1ccc0eefebdd6a4d90f00dfc682e46f08c4298ae88046412",
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
