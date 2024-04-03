pkgname = "fonts-font-awesome-otf"
pkgver = "6.5.2"
pkgrel = 0
pkgdesc = "Iconic font set"
maintainer = "triallax <triallax@tutanota.com>"
license = "OFL-1.1"
url = "https://fontawesome.com"
source = f"https://github.com/FortAwesome/Font-Awesome/releases/download/{pkgver}/fontawesome-free-{pkgver}-desktop.zip"
sha256 = "6392bc956eb3d391c9d7a14e891ce8010226ffc0c75f1338db126f13cb9cb8f4"


def do_install(self):
    for f in (self.cwd / "otfs").glob("*.otf"):
        self.install_file(
            f, "usr/share/fonts/font-awesome", name=f.name.replace(" ", "")
        )
