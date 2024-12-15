pkgname = "pdfjs"
pkgver = "4.9.155"
pkgrel = 1
pkgdesc = "Platform for parsing and rendering PDFs"
maintainer = "ttyyls <contact@behri.org>"
license = "Apache-2.0"
url = "https://github.com/mozilla/pdf.js"
source = f"{url}/releases/download/v{pkgver}/pdfjs-{pkgver}-legacy-dist.zip"
sha256 = "0f4778090298eb36c569b78ea4e9ca643ef9bfddb090f22464604c08b6256f73"
# no tests defined
options = ["!check"]


def install(self):
    self.install_files("web", "usr/share/pdf.js")
    self.install_files("build", "usr/share/pdf.js")
