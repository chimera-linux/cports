pkgname = "pdfjs"
pkgver = "4.5.136"
pkgrel = 0
pkgdesc = "Platform for parsing and rendering PDFs"
maintainer = "ttyyls <contact@behri.org>"
license = "Apache-2.0"
url = "https://github.com/mozilla/pdf.js"
source = f"{url}/releases/download/v{pkgver}/pdfjs-{pkgver}-dist.zip"
sha256 = "f5ca73a73d85b1dd9db9ee20188d4562d5852a859d1af0e414d0167c86e9ff64"
# no tests defined
options = ["!check"]


def install(self):
    self.install_files("web", "usr/share/pdf.js")
    self.install_files("build", "usr/share/pdf.js")
