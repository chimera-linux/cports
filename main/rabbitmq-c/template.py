pkgname = "rabbitmq-c"
pkgver = "0.15.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_STATIC_LIBS=ON",
    "-DBUILD_SHARED_LIBS=ON",
    "-DENABLE_SSL_SUPPORT=ON",
    "-DBUILD_TESTS=ON",
    "-DBUILD_TOOLS=ON",
]
hostmakedepends = ["cmake", "ninja", "pkgconf", "doxygen", "xmlto"]
makedepends = ["openssl3-devel", "popt-devel"]
pkgdesc = "RabbitMQ C client"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/alanxz/rabbitmq-c"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "7b652df52c0de4d19ca36c798ed81378cba7a03a0f0c5d498881ae2d79b241c2"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("rabbitmq-c-devel")
def _(self):
    return self.default_devel()


@subpackage("rabbitmq-c-progs")
def _(self):
    return self.default_progs()
