pkgname = "pdfjs"
pkgver = "5.3.31"
pkgrel = 0
pkgdesc = "Platform for parsing and rendering PDFs"
license = "Apache-2.0"
url = "https://github.com/mozilla/pdf.js"
source = f"{url}/releases/download/v{pkgver}/pdfjs-{pkgver}-legacy-dist.zip"
sha256 = "9d058813dd630fdf2201ee30243e62b3a066d2fedc8fd4103c1a34d12a6066c4"
# no tests defined
options = ["!check"]


def install(self):
    self.install_files("web", "usr/share/pdf.js")
    self.install_files("build", "usr/share/pdf.js")
