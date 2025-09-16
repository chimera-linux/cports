pkgname = "wpaperd"
pkgver = "1.2.2"
pkgrel = 0
build_style = "cargo"
make_build_args = ["--no-default-features", "--features", "avif"]
make_check_args = [*make_build_args]
hostmakedepends = [
    "cargo-auditable",
    "pkgconf",
    "scdoc",
]
makedepends = [
    "dav1d-devel",
    "dinit-chimera",
    "mesa-devel",
    "rust-std",
    "wayland-devel",
]
pkgdesc = "Wallpaper daemon for Wayland"
license = "GPL-3.0-or-later"
url = "https://github.com/danyspin97/wpaperd"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "16320b90cadd7a8ba7498b89d6142e47dcffcc8ea8ace04b28f8793d2c313ddf"
# check: no meaningful tests
options = ["!check"]


def post_build(self):
    with open(f"{self.cwd}/man/wpaperd-output.5.scd", "rb") as i:
        with open(f"{self.cwd}/wpaperd-output.5", "w") as o:
            self.do("scdoc", input=i.read(), stdout=o)


def install(self):
    self.install_license("LICENSE.md")
    self.install_man("wpaperd-output.5")
    self.install_service(self.files_path / "wpaperd.user")
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
