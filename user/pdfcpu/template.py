pkgname = "pdfcpu"
pkgver = "0.10.2"
pkgrel = 3
build_style = "go"
make_build_args = ["-ldflags", f"-X main.commit=v{pkgver}", "./cmd/pdfcpu"]
make_check_args = ["-p", "1", "./..."]
hostmakedepends = ["go"]
pkgdesc = "PDF processor written in Go"
license = "Apache-2.0"
url = "https://pdfcpu.io"
source = f"https://github.com/pdfcpu/pdfcpu/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "a07cc50446ef6526fa26d5fe2c9e207724971e0b6917f3d70680ec39cfc53aec"
# check may be disabled
options = []

if self.profile().wordsize == 32:
    # invalid RSA public exponent
    options += ["!check"]
