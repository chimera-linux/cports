pkgname = "pdfjs"
pkgver = "4.6.82"
pkgrel = 0
pkgdesc = "Platform for parsing and rendering PDFs"
maintainer = "ttyyls <contact@behri.org>"
license = "Apache-2.0"
url = "https://github.com/mozilla/pdf.js"
source = f"{url}/releases/download/v{pkgver}/pdfjs-{pkgver}-dist.zip"
sha256 = "19d061ca742362ce3c1553a0841ec1be9c1f0d86d6a39799569bff38da1764be"
# no tests defined
options = ["!check"]


def install(self):
    self.install_files("web", "usr/share/pdf.js")
    self.install_files("build", "usr/share/pdf.js")
