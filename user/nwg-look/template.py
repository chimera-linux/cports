pkgname = "nwg-look"
pkgver = "1.2.1"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go", "pkgconf"]
makedepends = ["gtk+3-devel"]
depends = ["libcanberra-gtk3", "xcur2png"]
pkgdesc = "GTK settings editor for wlroots"
license = "MIT"
url = "https://github.com/nwg-piotr/nwg-look"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "1c66053f559f1756b18b615987a450433117c6b6c08759debdef94b6fd906480"
# ppc disables pie
hardening = []

match self.profile.arch:
    case "ppc64le" | "ppc64":
        # https://github.com/golang/go/issues/82324
        hardening += ["!pie"]


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
