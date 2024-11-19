pkgname = "fonts-font-awesome-otf"
pkgver = "6.7.0"
pkgrel = 0
pkgdesc = "Iconic font set"
maintainer = "triallax <triallax@tutanota.com>"
license = "OFL-1.1"
url = "https://fontawesome.com"
source = f"https://github.com/FortAwesome/Font-Awesome/releases/download/{pkgver}/fontawesome-free-{pkgver}-desktop.zip"
sha256 = "0494ff2d3b05dff36e4e72204aa1a98fdee24a78fede6005f882e28d46037b28"


def install(self):
    for f in (self.cwd / "otfs").glob("*.otf"):
        self.install_file(
            f, "usr/share/fonts/font-awesome", name=f.name.replace(" ", "")
        )
    self.install_license("LICENSE.txt")
