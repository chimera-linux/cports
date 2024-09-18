pkgname = "fonts-font-awesome-otf"
pkgver = "6.6.0"
pkgrel = 1
pkgdesc = "Iconic font set"
maintainer = "triallax <triallax@tutanota.com>"
license = "OFL-1.1"
url = "https://fontawesome.com"
source = f"https://github.com/FortAwesome/Font-Awesome/releases/download/{pkgver}/fontawesome-free-{pkgver}-desktop.zip"
sha256 = "8cde9bf442f218ee330844263ee35403ff466a1afbbd11ab170523f3cd09067c"


def install(self):
    for f in (self.cwd / "otfs").glob("*.otf"):
        self.install_file(
            f, "usr/share/fonts/font-awesome", name=f.name.replace(" ", "")
        )
    self.install_license("LICENSE.txt")
