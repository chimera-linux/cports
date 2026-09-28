pkgname = "fonts-source-serif-otf"
pkgver = "4.005"
pkgrel = 0
pkgdesc = "Companion serif font family for Source Sans"
license = "OFL-1.1"
url = "https://adobe-fonts.github.io/source-serif"
source = f"https://github.com/adobe-fonts/source-serif/releases/download/{pkgver}R/source-serif-{pkgver}_Desktop.zip"
sha256 = "549fdb8f9a682bd06944298621404969f6de77c2e422ff3b8244a1dcd6a0c425"


def install(self):
    self.install_file(
        f"source-serif-{pkgver}_Desktop/OTF/*.otf",
        "usr/share/fonts/source-serif",
        glob=True,
    )
    self.install_license(f"source-serif-{pkgver}_Desktop/LICENSE.md")
