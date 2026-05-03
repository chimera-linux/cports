pkgname = "uad-ng"
pkgver = "1.2.0"
pkgrel = 0
build_style = "cargo"
make_build_args = ["--no-default-features", "--features", "wgpu"]
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = [
    "fontconfig-devel",
    "libx11-devel",
    "libxcursor-devel",
    "libxi-devel",
    "libxkbcommon-devel",
    "libxrandr-devel",
    "rust-std",
    "wayland-devel",
]
depends = ["android-tools"]
pkgdesc = "Cross-platform GUI debloater for Android devices"
license = "GPL-3.0-only"
url = "https://github.com/Universal-Debloater-Alliance/universal-android-debloater-next-generation"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "455fd89ed5f57cb895d213d60e6acefcf0d779fcbc982e31c0f0acb085909430"


def post_install(self):
    self.install_license("LICENSE")
    self.install_file(
        "resources/assets/logo-dark.png",
        "usr/share/icons/hicolor/400x400/apps",
        name="uad-ng.png",
    )
    self.install_file(
        self.files_path / "uad-ng.desktop",
        "usr/share/applications",
    )
