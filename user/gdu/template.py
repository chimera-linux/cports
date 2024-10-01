pkgname = "gdu"
pkgver = "5.29.0"
pkgrel = 2
build_style = "go"
make_build_args = ["./cmd/gdu"]
# expects writing to /xyzxyz to give eperm instead of erofs (which happens in --ro bwrap)
make_check_args = ["-skip", "TestOutputFileError", "./..."]
hostmakedepends = ["go"]
pkgdesc = "Disk usage analyzer"
maintainer = "tulilirockz <tulilirockz@outlook.com>"
license = "MIT"
url = "https://github.com/dundee/gdu"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "42e972f46e49995be24b223c91375bfbea547f5e8cf94c0364f7b3eb5b0ed0a3"


def post_install(self):
    self.install_man("gdu.1")
    self.install_license("LICENSE.md")
