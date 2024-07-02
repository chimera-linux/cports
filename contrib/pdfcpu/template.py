pkgname = "pdfcpu"
pkgver = "0.8.0"
_commit = "576f15e"
pkgrel = 3
build_style = "go"
make_build_args = ["-ldflags", f"-X main.commit={_commit}", "./cmd/pdfcpu"]
make_check_args = ["-p", "1", "./..."]
hostmakedepends = ["go"]
pkgdesc = "PDF processor written in Go"
maintainer = "Subhaditya Nath <sn03.general@gmail.com>"
license = "Apache-2.0"
url = "https://pdfcpu.io"
source = f"https://github.com/pdfcpu/pdfcpu/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "38fa9db4e6d2ad1dfe533acd26c12a56b5940ae3ec4d57fee927b6bc9d223359"
