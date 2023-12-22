pkgname = "fonts-font-awesome-otf"
pkgver = "6.5.1"
pkgrel = 0
pkgdesc = "Iconic font set"
maintainer = "triallax <triallax@tutanota.com>"
license = "OFL-1.1"
url = "https://fontawesome.com"
source = f"https://github.com/FortAwesome/Font-Awesome/releases/download/{pkgver}/fontawesome-free-{pkgver}-desktop.zip"
sha256 = "88d13abdade8b24b5fbdf6fe7d3ee55507d2827be91990a066ed96b8a2a58003"


def do_install(self):
    for f in (self.cwd / "otfs").glob("*.otf"):
        self.install_file(
            f, "usr/share/fonts/font-awesome", name=f.name.replace(" ", "")
        )
