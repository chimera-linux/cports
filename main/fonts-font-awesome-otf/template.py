pkgname = "fonts-font-awesome-otf"
pkgver = "6.7.2"
pkgrel = 0
pkgdesc = "Iconic font set"
maintainer = "triallax <triallax@tutanota.com>"
license = "OFL-1.1"
url = "https://fontawesome.com"
source = f"https://github.com/FortAwesome/Font-Awesome/releases/download/{pkgver}/fontawesome-free-{pkgver}-desktop.zip"
sha256 = "22ff7898b429b997a45e1cf89bb869ed3abcc65333d90289181ba5363c8fd19b"


def install(self):
    for f in (self.cwd / "otfs").glob("*.otf"):
        self.install_file(
            f, "usr/share/fonts/font-awesome", name=f.name.replace(" ", "")
        )
    self.install_license("LICENSE.txt")
