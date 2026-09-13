pkgname = "fonts-font-awesome-otf"
pkgver = "7.3.1"
pkgrel = 0
pkgdesc = "Iconic font set"
license = "OFL-1.1"
url = "https://fontawesome.com"
source = f"https://github.com/FortAwesome/Font-Awesome/releases/download/{pkgver}/fontawesome-free-{pkgver}-desktop.zip"
sha256 = "c61edde261707f33376a28e9a30bb8c70c1a20bf0bd975206b809f3b3b70add5"


def install(self):
    for f in (self.cwd / "otfs").glob("*.otf"):
        self.install_file(
            f, "usr/share/fonts/font-awesome", name=f.name.replace(" ", "")
        )
    self.install_license("LICENSE.txt")
