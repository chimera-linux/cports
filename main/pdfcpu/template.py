pkgname = "pdfcpu"
pkgver = "0.9.1"
pkgrel = 0
build_style = "go"
make_build_args = ["-ldflags", f"-X main.commit=v{pkgver}", "./cmd/pdfcpu"]
make_check_args = ["-p", "1", "./..."]
hostmakedepends = ["go"]
pkgdesc = "PDF processor written in Go"
maintainer = "Subhaditya Nath <sn03.general@gmail.com>"
license = "Apache-2.0"
url = "https://pdfcpu.io"
source = f"https://github.com/pdfcpu/pdfcpu/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "79572e599deddfaa72109f3e029b74b8cd6070657355e8cc9d8c7fb91da73c71"
