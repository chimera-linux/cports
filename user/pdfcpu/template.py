pkgname = "pdfcpu"
pkgver = "0.11.0"
pkgrel = 2
build_style = "go"
make_build_args = ["-ldflags", f"-X main.commit=v{pkgver}", "./cmd/pdfcpu"]
make_check_args = ["-p", "1", "./..."]
hostmakedepends = ["go"]
pkgdesc = "PDF processor written in Go"
license = "Apache-2.0"
url = "https://pdfcpu.io"
source = f"https://github.com/pdfcpu/pdfcpu/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "16e6e4fbcf809f9d737d8931c267220e5e4cb00fbce793eeaa4501193b954c55"
# check may be disabled
options = []

if self.profile().wordsize == 32:
    # invalid RSA public exponent
    options += ["!check"]
