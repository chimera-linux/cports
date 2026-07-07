pkgname = "libfyaml"
pkgver = "0.9.6"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-network"]
hostmakedepends = ["autoconf", "automake", "pkgconf", "libtool"]
makedepends = ["linux-headers"]
checkdepends = ["bash", "check-devel", "git"]
pkgdesc = "YAML parser and emitter"
license = "MIT"
url = "https://github.com/pantoniou/libfyaml"
source = f"{url}/releases/download/v{pkgver}/libfyaml-{pkgver}.tar.gz"
sha256 = "a59cc3331e2eb903ec36933ad52a45888041cac31e44f553a00511131242c483"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libfyaml-progs")
def _(self):
    return self.default_progs()


@subpackage("libfyaml-devel")
def _(self):
    return self.default_devel()
