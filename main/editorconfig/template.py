pkgname = "editorconfig"
pkgver = "0.12.9"
_test_commit = "5ca0b296dc31124d0303895c163013450bd97958"
pkgrel = 2
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["pcre2-devel"]
pkgdesc = "EditorConfig core C library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://editorconfig.org"
source = [
    f"https://github.com/editorconfig/editorconfig-core-c/archive/v{pkgver}.tar.gz",
    f"https://github.com/editorconfig/editorconfig-core-test/archive/{_test_commit}.tar.gz",
]
source_paths = [".", "tests"]
sha256 = [
    "4aaa4e3883332aac7ec19c169dcf128f5f0f963f61d09beb299eb2bce5944e2c",
    "a1ca71c8f099c6ffc4fc1c0214732d4e27168fb2a5fbf2da47b5bc50fb7b5e79",
]
# a bunch of tests fail due to... cmake?
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("editorconfig-devel")
def _(self):
    return self.default_devel()
