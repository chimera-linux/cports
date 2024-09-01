pkgname = "wpaperd"
pkgver = "1.0.1"
pkgrel = 1
build_style = "cargo"
hostmakedepends = [
    "cargo-auditable",
    "pkgconf",
    "scdoc",
]
makedepends = ["mesa-devel", "rust-std", "wayland-devel"]
pkgdesc = "Wallpaper daemon for Wayland"
maintainer = "tulilirockz <tulilirockz@outlook.com>"
license = "GPL-3.0-or-later"
url = "https://github.com/danyspin97/wpaperd"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "4ed30c90dc14fa629ac977ace3ca4a146a33d85f73d2d49915643fbb9ea53ab9"
# check: no meaningful tests
options = ["!check"]


def post_build(self):
    with open(f"{self.cwd}/man/wpaperd-output.5.scd", "rb") as i:
        with open(f"{self.cwd}/wpaperd-output.5", "w") as o:
            self.do("scdoc", input=i.read(), stdout=o)


def install(self):
    self.install_license("LICENSE.md")
    self.install_man("wpaperd-output.5")
    with self.pushd(f"target/{self.profile().triplet}/release"):
        self.install_bin("wpaperd")
        self.install_bin("wpaperctl")
        with self.pushd("completions"):
            self.install_completion("wpaperd.bash", "bash")
            self.install_completion("wpaperd.fish", "fish")
            self.install_completion("_wpaperd", "zsh")
            self.install_completion("wpaperctl.bash", "bash", "wpaperctl")
            self.install_completion("_wpaperctl", "zsh", "wpaperctl")
            self.install_completion("wpaperctl.fish", "fish", "wpaperctl")
