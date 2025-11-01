pkgname = "pdfjs"
pkgver = "5.4.296"
pkgrel = 0
pkgdesc = "Platform for parsing and rendering PDFs"
license = "Apache-2.0"
url = "https://github.com/mozilla/pdf.js"
source = f"{url}/releases/download/v{pkgver}/pdfjs-{pkgver}-legacy-dist.zip"
sha256 = "9085d6a3f5b494341aed440aeed61c61304b6acacbf04ddd90639765d51c7949"
# no tests defined
options = ["!check"]


def install(self):
    self.install_files("web", "usr/share/pdf.js")
    self.install_files("build", "usr/share/pdf.js")
