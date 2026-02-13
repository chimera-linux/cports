pkgname = "wl-screenrec"
pkgver = "0.2.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = [
    "cargo-auditable",
    "pkgconf",
]
makedepends = [
    "ffmpeg-devel",
    "libdrm-devel",
    "rust-std",
    "vulkan-headers",
]
pkgdesc = "High performance wlroots screen recorder"
license = "Apache-2.0"
url = "https://github.com/russelltg/wl-screenrec"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "214cbd9c74a57f980eacb6623743dea94f20b2f3fcea4705cec2b865b5f84fbb"
hardening = ["vis", "cfi"]
# checks require a wayland compositor to be running
options = ["!check", "!cross"]


def post_build(self):
    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"wl-screenrec.{shell}", "w") as f:
            self.do(
                f"./target/{self.profile().triplet}/release/wl-screenrec",
                "--generate-completions",
                shell,
                stdout=f,
            )


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/wl-screenrec")
    self.install_license("LICENSE")
    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"wl-screenrec.{shell}", shell, "wl-screenrec")
