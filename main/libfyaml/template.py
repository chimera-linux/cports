pkgname = "libfyaml"
pkgver = "0.9"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-network"]
configure_gen = []
hostmakedepends = ["pkgconf"]
makedepends = ["linux-headers"]
checkdepends = ["bash", "check-devel", "git"]
pkgdesc = "YAML parser and emitter"
license = "MIT"
url = "https://github.com/pantoniou/libfyaml"
source = f"{url}/releases/download/v{pkgver}/libfyaml-{pkgver}.tar.gz"
sha256 = "7731edc5dfcc345d5c5c9f6ce597133991a689dabede393cd77bae89b327cd6d"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libfyaml-progs")
def _(self):
    return self.default_progs()


@subpackage("libfyaml-devel")
def _(self):
    return self.default_devel()
