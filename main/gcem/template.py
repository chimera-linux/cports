pkgname = "gcem"
pkgver = "1.18.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DCMAKE_POLICY_VERSION_MINIMUM=3.5",
    "-DGCEM_BUILD_TESTS=1",
]
make_build_target = "gcem_tests"
hostmakedepends = ["cmake", "ninja"]
pkgdesc = "C++ compile-time math library"
license = "Apache-2.0"
url = "https://github.com/kthohr/gcem"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "8e71a9f5b62956da6c409dda44b483f98c4a98ae72184f3aa4659ae5b3462e61"


def check(self):
    self.do("sh", "../../tests/run_tests", wrksrc="build/tests")
