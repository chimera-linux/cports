pkgname = "pdfjs"
pkgver = "4.8.69"
pkgrel = 0
pkgdesc = "Platform for parsing and rendering PDFs"
maintainer = "ttyyls <contact@behri.org>"
license = "Apache-2.0"
url = "https://github.com/mozilla/pdf.js"
source = f"{url}/releases/download/v{pkgver}/pdfjs-{pkgver}-dist.zip"
sha256 = "887a6e5f0cda2136daf99cc5ae5fe34581c7bfef2ce64f5c27963d965d88d2c6"
# no tests defined
options = ["!check"]


def install(self):
    self.install_files("web", "usr/share/pdf.js")
    self.install_files("build", "usr/share/pdf.js")
