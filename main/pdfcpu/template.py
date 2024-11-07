pkgname = "pdfcpu"
pkgver = "0.8.1"
pkgrel = 3
build_style = "go"
make_build_args = ["-ldflags", f"-X main.commit=v{pkgver}", "./cmd/pdfcpu"]
make_check_args = ["-p", "1", "./..."]
hostmakedepends = ["go"]
pkgdesc = "PDF processor written in Go"
maintainer = "Subhaditya Nath <sn03.general@gmail.com>"
license = "Apache-2.0"
url = "https://pdfcpu.io"
source = f"https://github.com/pdfcpu/pdfcpu/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "965624c0d714d8ae2c3db06874ae37973d37bb7815ea4eeec7c761ffc6143a1a"
