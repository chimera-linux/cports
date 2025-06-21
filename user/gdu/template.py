pkgname = "gdu"
pkgver = "5.30.1"
pkgrel = 6
build_style = "go"
make_build_args = ["./cmd/gdu"]
# expects writing to /xyzxyz to give eperm instead of erofs (which happens in --ro bwrap)
make_check_args = ["-skip", "TestOutputFileError", "./..."]
hostmakedepends = ["go"]
pkgdesc = "Disk usage analyzer"
license = "MIT"
url = "https://github.com/dundee/gdu"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "ad363967b6a34e02812e4cba36bb340f377cf64a435e23f6e8e9e6b3f775220e"
# check may be disabled
options = []

# err: while opening file: /tmp/badger/000003.vlog err: cannot allocate memory
if self.profile().wordsize == 32:
    options += ["!check"]


def post_install(self):
    self.install_man("gdu.1")
    self.install_license("LICENSE.md")
