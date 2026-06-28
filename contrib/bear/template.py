pkgname = "bear"
pkgver = "3.1.4"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DENABLE_UNIT_TESTS=ON",
    "-DENABLE_FUNC_TESTS=OFF",  # need lit https://pypi.org/project/lit
]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    "fmt-devel",
    "grpc-devel",
    "gtest-devel",
    "nlohmann-json",
    "spdlog-devel",
]
pkgdesc = "Tool that generates a compilation database"
maintainer = "sonata-chen <sonatachen39@gmail.com>"
license = "GPL-3.0-or-later"
url = "https://github.com/rizsotto/Bear"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "a1105023795b3e1b9abc29c088cdec5464cc9f3b640b5078dc90a505498da5ff"
