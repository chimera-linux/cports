pkgname = "mingw-w64-pkg-config"
pkgver = "1.0.0"
pkgrel = 0
build_style = "meta"
depends = ["cmd:pkg-config!pkgconf"]
pkgdesc = "Support pkg-config script for Windows development"
license = "custom:meta"
url = "http://pkg-config.freedesktop.org"

_targets = ["x86_64", "i686", "aarch64", "armv7"]


def install(self):
    for an in _targets:
        at = an + "-w64-mingw32"
        self.install_bin(
            self.files_path / "mingw-pkgconfig.sh",
            name=f"{at}-pkg-config",
        )
