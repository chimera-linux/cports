pkgname = "nwg-look"
pkgver = "1.1.2"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go", "pkgconf"]
makedepends = ["gtk+3-devel"]
depends = ["xcur2png"]
pkgdesc = "GTK settings editor for wlroots"
license = "MIT"
url = "https://github.com/nwg-piotr/nwg-look"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "2db9bf20042beec0e9e9bba5769c08e34197e3a0da595b743c39b384aa0e0af0"


def install(self):
    self.install_bin("build/nwg-look")
    self.install_license("LICENSE")
    self.install_file("stuff/main.glade", "usr/share/nwg-look")
    self.install_files("langs", "usr/share/nwg-look")
    self.install_file("stuff/nwg-look.desktop", "usr/share/applications")
    self.install_file(
        "stuff/nwg-look.svg",
        "usr/share/icons/hicolor/scalable/apps",
    )
