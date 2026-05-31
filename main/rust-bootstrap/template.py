pkgname = "rust-bootstrap"
pkgver = "1.95.0"
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
            "483b562243d0f9e180f76c9ca6144fd9bb17413429c655e94b6b50bfaa20a86b",
            "cf9b751c7113c95e9f387c3713715f9e2b93d5c9561ea22659d9dc646cbecb1d",
        ]
    case "loongarch64":
        sha256 = [
            "44cb9571efb2862f8b6d8e7bf4aad18cd3e4613ad93316bd8e7dde16053f79a2",
            "f35fbdf5b3b007e19b735d3c9597d7f06a3c7dd1d3b233b333e1784bc143c4bf",
        ]
    case "ppc64le":
        sha256 = [
            "2f621bf2e8fa7f03717b0017d3843e5fef35731a383e33204fcdfab053cba236",
            "74480581f1398a7fcbc7e94dfa6ae4d46f69b6d6527b680200202284cece92e4",
        ]
    case "ppc64":
        sha256 = [
            "ea43e9891d85522d9994791f0ba8f26ded2a07bb642860c7e666ee9e70fbc309",
            "25858a05b5acc15b52ad50e4443a43a49ff9f8b6f00482dddc95f273b7a85755",
        ]
    case "ppc":
        sha256 = [
            "fc537d46d06df0554f719232693408db690c788f2c5a128680eaffea81025a9a",
            "e8e5d62385a04c93ce9fdfb4a3b074ca947746f6567b2457a746783b18198c00",
        ]
    case "riscv64":
        sha256 = [
            "9780f396991d2e4ff4d497ada812e06a14ecd00e410b05c06ab3c842739895e0",
            "93371390a5196c257b1146a2b3d638902a8a04d430fc48dc9dc08041147cc0c8",
        ]
    case "x86_64":
        sha256 = [
            "b1f3183ec54382c5ed73478c135244198b6c935f2ca59e08c20eb609f47a3298",
            "99f256c31aac502ba736baee9e13b26b061fa76a34e827dac94a50d69035f2ef",
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
