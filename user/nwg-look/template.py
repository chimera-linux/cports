pkgname = "nwg-look"
pkgver = "1.1.1"
pkgrel = 1
build_style = "go"
hostmakedepends = ["go", "pkgconf"]
makedepends = ["gtk+3-devel"]
depends = ["xcur2png"]
pkgdesc = "GTK settings editor for wlroots"
license = "MIT"
url = "https://github.com/nwg-piotr/nwg-look"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "568c5efe443892d74ffce6cf8ac7db2aea6071be70d97d3ba7c5efd8b351e601"


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
