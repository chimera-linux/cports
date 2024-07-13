pkgname = "pdfjs"
pkgver = "4.4.168"
pkgrel = 0
pkgdesc = "Platform for parsing and rendering PDFs"
maintainer = "ttyyls <contact@behri.org>"
license = "Apache-2.0"
url = "https://github.com/mozilla/pdf.js"
source = f"{url}/releases/download/v{pkgver}/pdfjs-{pkgver}-dist.zip"
sha256 = "69ce8f314bdc0035e3bca922e5f9260d8815f85ae693d1394f361ed075fb696c"
# no tests defined
options = ["!check"]


def do_install(self):
    self.install_files("web", "usr/share/pdf.js")
    self.install_files("build", "usr/share/pdf.js")
