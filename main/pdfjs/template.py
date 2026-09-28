pkgname = "pdfjs"
pkgver = "5.7.284"
pkgrel = 0
pkgdesc = "Platform for parsing and rendering PDFs"
license = "Apache-2.0"
url = "https://github.com/mozilla/pdf.js"
source = f"{url}/releases/download/v{pkgver}/pdfjs-{pkgver}-legacy-dist.zip"
sha256 = "b1edded128a7e50e7818bfe16564eb4012dd3f13f2847f9f94100c96567afbcc"
# no tests defined
options = ["!check"]


def install(self):
    self.install_files("web", "usr/share/pdf.js")
    self.install_files("build", "usr/share/pdf.js")
