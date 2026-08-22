pkgname = "lact"
pkgver = "0.10.0"
pkgrel = 0
archs = ["x86_64"]
build_style = "cargo"
prepare_after_patch = True
make_build_args = [
    "--no-default-features",
    "--features=lact-gui,display-info",
]
make_check_args = [
    *make_build_args,
    "--",
    "--skip=tests::apply_settings",  # fails in container, but passes outside of it
]
hostmakedepends = [
    "cargo",
    "pkgconf",
]
makedepends = [
    "gtk4-devel",
    "libadwaita-devel",
    "libdisplay-info-devel",
    "libdrm-devel",
]
depends = [
    "hwdata-pci",
]
pkgdesc = "GPU Configuration and Monitoring Tool"
license = "MIT"
url = "https://github.com/ilya-zlobintsev/LACT"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "4bb1a5066fe2071acee72b0c813e087c9a3060bc35f5e3ec4909fb4cb3e69ea0"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/lact")
    self.install_file(
        "res/io.github.ilya_zlobintsev.LACT.desktop", "usr/share/applications"
    )
    self.install_file(
        "res/io.github.ilya_zlobintsev.LACT.png", "usr/share/icons"
    )
    self.install_file(
        "res/io.github.ilya_zlobintsev.LACT.svg",
        "usr/share/icons/hicolor/scalable/apps",
    )
    self.install_service(self.files_path / "lactd")
    self.install_license("LICENSE")
