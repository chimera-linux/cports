pkgname = "protobuf"
pkgver = "24.2"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-Dprotobuf_BUILD_TESTS=OFF",
    "-Dprotobuf_ABSL_PROVIDER=package",
    "-DBUILD_SHARED_LIBS=ON",
]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["abseil-cpp-devel"]
pkgdesc = "Google's data interchange format"
maintainer = "roastveg <louis@hamptonsoftworks.com>"
license = "BSD-3-Clause"
url = "https://github.com/protocolbuffers/protobuf"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "39b52572da90ad54c883a828cb2ca68e5ac918aa75d36c3e55c9c76b94f0a4f7"


def post_install(self):
    self.install_license("LICENSE")


@subpackage(f"{pkgname}-static")
def _static(self):
    return self.default_static()
