pkgname = "nwg-look"
pkgver = "1.1.1"
pkgrel = 0
build_style = "go"
hostmakedepends = [
    "go",
    "pkgconf",
]
makedepends = [
    "gtk+3-devel",
]
depends = ["gsettings-desktop-schemas", "xcur2png"]
pkgdesc = "GTK3 settings editor adapted to work in the wlroots environment"
license = "MIT"
url = "https://github.com/nwg-piotr/nwg-look"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "568c5efe443892d74ffce6cf8ac7db2aea6071be70d97d3ba7c5efd8b351e601"


def install(self):
    self.install_bin(f"build/{pkgname}")
    self.install_license("LICENSE")
    self.install_file("stuff/main.glade", f"usr/share/{pkgname}")
    self.install_files("langs", f"usr/share/{pkgname}", name="langs")
    self.install_file(f"stuff/{pkgname}.desktop", "usr/share/applications")
    self.install_file(
        f"stuff/{pkgname}.svg",
        "usr/share/icons/hicolor/scalable/apps",
    )
