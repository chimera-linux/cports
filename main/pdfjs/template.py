pkgname = "pdfjs"
pkgver = "4.9.155"
pkgrel = 0
pkgdesc = "Platform for parsing and rendering PDFs"
maintainer = "ttyyls <contact@behri.org>"
license = "Apache-2.0"
url = "https://github.com/mozilla/pdf.js"
source = f"{url}/releases/download/v{pkgver}/pdfjs-{pkgver}-dist.zip"
sha256 = "1059ba50947a634a531d0bcbef77532020f43811e7996415f502829ec1cc925f"
# no tests defined
options = ["!check"]


def install(self):
    self.install_files("web", "usr/share/pdf.js")
    self.install_files("build", "usr/share/pdf.js")
