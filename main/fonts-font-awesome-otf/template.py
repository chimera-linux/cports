pkgname = "fonts-font-awesome-otf"
pkgver = "6.7.1"
pkgrel = 0
pkgdesc = "Iconic font set"
maintainer = "triallax <triallax@tutanota.com>"
license = "OFL-1.1"
url = "https://fontawesome.com"
source = f"https://github.com/FortAwesome/Font-Awesome/releases/download/{pkgver}/fontawesome-free-{pkgver}-desktop.zip"
sha256 = "3118838d8d0aa88b8c9a5e132f8a195a3f1b23895ae66c61dc6746f9ceef80da"


def install(self):
    for f in (self.cwd / "otfs").glob("*.otf"):
        self.install_file(
            f, "usr/share/fonts/font-awesome", name=f.name.replace(" ", "")
        )
    self.install_license("LICENSE.txt")
