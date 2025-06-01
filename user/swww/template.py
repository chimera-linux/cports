pkgname = "swww"
pkgver = "0.10.1"
pkgrel = 0
build_style = "cargo"
hostmakedepends = [
    "cargo-auditable",
    "pkgconf",
    "scdoc",
]
makedepends = [
    "lz4-devel",
    "rust-std",
    "wayland-devel",
    "wayland-protocols",
]
pkgdesc = "Solution to your Wayland Wallpaper Woes"
license = "GPL-3.0-only"
url = "https://github.com/LGFae/swww"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "ebfb174ce59340ff5c4a4c764dd035dd1b2bd8041c6d3c0e4733460c36286c52"

if self.profile().arch in ["loongarch64"]:
    broken = "cannot find value `MADV_SOFT_OFFLINE` in module `c`"


def post_build(self):
    self.do("./doc/gen.sh")


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/swww")
    self.install_bin(f"target/{self.profile().triplet}/release/swww-daemon")
    self.install_service(self.files_path / "swww.user")
    self.install_man("doc/generated/*", glob=True)
    with self.pushd("completions"):
        self.install_completion("swww.bash", "bash")
        self.install_completion("_swww", "zsh")
        self.install_completion("swww.fish", "fish")
