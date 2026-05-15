pkgname = "awww"
pkgver = "0.12.1"
pkgrel = 0
build_style = "cargo"
make_build_args = [
    "--no-default-features",
    "--features=avif",
    "--features=jxl",
]
hostmakedepends = [
    "cargo-auditable",
    "pkgconf",
    "scdoc",
]
makedepends = [
    "dav1d-devel",
    "dinit-chimera",
    "lz4-devel",
    "rust-std",
    "turnstile",
    "wayland-devel",
    "wayland-protocols",
]
renames = ["swww"]
pkgdesc = "Answer to your Wayland Wallpaper Woes"
license = "GPL-3.0-only"
url = "https://codeberg.org/LGFae/awww"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "5e31092d5170b90ec614f76bad0739b729923a57979d2dfed3673cf0d8db2dee"

match self.profile().arch:
    case "loongarch64":
        broken = "cannot find value `MADV_SOFT_OFFLINE` in module `c`"
    case "ppc64le" | "ppc64" | "ppc":
        broken = "uses rustix experimental runtime module, unavailable"


def post_build(self):
    self.do("./doc/gen.sh")


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/awww")
    self.install_bin(f"target/{self.profile().triplet}/release/awww-daemon")
    self.install_service(self.files_path / "awww.user")
    self.install_man("doc/generated/*", glob=True)
    with self.pushd("completions"):
        self.install_completion("awww.bash", "bash")
        self.install_completion("_awww", "zsh")
        self.install_completion("awww.fish", "fish")
