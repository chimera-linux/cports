pkgname = "pdfjs"
pkgver = "5.4.54"
pkgrel = 0
pkgdesc = "Platform for parsing and rendering PDFs"
license = "Apache-2.0"
url = "https://github.com/mozilla/pdf.js"
source = f"{url}/releases/download/v{pkgver}/pdfjs-{pkgver}-legacy-dist.zip"
sha256 = "cebbae3903847088be128ddcdd7243eae2985fdc9b553e5b4519282624443df9"
# no tests defined
options = ["!check"]


def install(self):
    self.install_files("web", "usr/share/pdf.js")
    self.install_files("build", "usr/share/pdf.js")
