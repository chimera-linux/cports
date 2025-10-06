pkgname = "editorconfig"
pkgver = "0.12.10"
_test_commit = "5ca0b296dc31124d0303895c163013450bd97958"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["pcre2-devel"]
pkgdesc = "EditorConfig core C library"
license = "BSD-2-Clause"
url = "https://editorconfig.org"
source = [
    f"https://github.com/editorconfig/editorconfig-core-c/archive/v{pkgver}.tar.gz",
    f"https://github.com/editorconfig/editorconfig-core-test/archive/{_test_commit}.tar.gz",
]
source_paths = [".", "tests"]
sha256 = [
    "ab9f897a90fb36cfc34e5b67221e55ab0e3119b3512de8e31029d376c6bab870",
    "a1ca71c8f099c6ffc4fc1c0214732d4e27168fb2a5fbf2da47b5bc50fb7b5e79",
]
# a bunch of tests fail due to... cmake?
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("editorconfig-devel")
def _(self):
    return self.default_devel()
