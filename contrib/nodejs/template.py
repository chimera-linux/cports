pkgname = "nodejs"
pkgver = "18.12.1"
pkgrel = 0
build_style = "configure"
configure_args = [
    "--shared-zlib", "--shared-openssl", "--shared-libuv", "--shared-nghttp2",
    "--shared-cares", "--shared-brotli", "--with-intl=system-icu",
    "--openssl-use-def-ca-store", "--ninja", "--prefix=/usr",
]
make_cmd = "gmake"
make_check_target = "test-only"
hostmakedepends = [
    "pkgconf", "ninja", "python", "gmake", "python-jinja2",
]
makedepends = [
    "zlib-devel", "icu-devel", "openssl-devel", "libuv-devel",
    "nghttp2-devel", "c-ares-devel", "brotli-devel", "linux-headers",
]
checkdepends = ["procps-ng", "iana-etc"]
pkgdesc = "JavaScript runtime based on V8"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://nodejs.org"
source = f"{url}/dist/v{pkgver}/node-v{pkgver}.tar.gz"
sha256 = "ba8174dda00d5b90943f37c6a180a1d37c861d91e04a4cb38dc1c0c74981c186"
debug_level = 1 # allow LTO build to not run out of mem
options = ["!cross"]

def post_extract(self):
    self.mv("deps/openssl/nodejs-openssl.cnf", ".")

    for f in [
        "deps/brotli", "deps/cares", "deps/openssl", "deps/zlib",
        "deps/v8/third_party/jinja2", "tools/inspector_protocol/jinja2",
    ]:
        self.rm(f, recursive = True)

    self.mkdir("deps/openssl")
    self.mv("nodejs-openssl.cnf", "deps/openssl")

def post_install(self):
    self.install_license("LICENSE")

# real test suite requires network acccess
def do_check(self):
    npath = self.chroot_cwd / "out/Release"
    nexe = npath / "node"
    self.do(nexe, "-e", "console.log('test')", wrksrc = "out/Release")
    self.do(
        nexe, "-e",
        f"require('assert').equal(process.versions.node, '{pkgver}')",
        wrksrc = "out/Release"
    )

@subpackage("nodejs-devel")
def _devel(self):
    return self.default_devel()

# FIXME visibility
hardening = ["!vis"]
