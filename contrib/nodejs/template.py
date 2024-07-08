pkgname = "nodejs"
pkgver = "22.4.1"
pkgrel = 0
build_style = "configure"
configure_args = [
    "--ninja",
    "--openssl-use-def-ca-store",
    "--prefix=/usr",
    "--shared-brotli",
    "--shared-cares",
    "--shared-libuv",
    "--shared-nghttp2",
    "--shared-openssl",
    "--shared-zlib",
    "--with-intl=system-icu",
]
make_cmd = "gmake"
make_check_target = "test-only"
hostmakedepends = [
    "pkgconf",
    "ninja",
    "python",
    "gmake",
    "python-jinja2",
]
makedepends = [
    "zlib-ng-compat-devel",
    "icu-devel",
    "openssl-devel",
    "libuv-devel",
    "nghttp2-devel",
    "c-ares-devel",
    "brotli-devel",
    "linux-headers",
]
checkdepends = ["procps"]
pkgdesc = "JavaScript runtime based on V8"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://nodejs.org"
source = f"{url}/dist/v{pkgver}/node-v{pkgver}.tar.gz"
sha256 = "b3051c3358c96d06dd17305c065cc6f5205c1f4d72dd42cb184f7ba79605f8a8"
debug_level = 1  # allow LTO build to not run out of mem
hardening = ["!cfi"]  # TODO
options = ["!cross"]

match self.profile().arch:
    case "ppc64le" | "ppc64" | "riscv64":
        # trap in add_label_offset() (assembler-ppc.cc)
        # also crashes on riscv64
        hardening += ["!int"]
    case "ppc":
        broken = "unsupported"


def post_extract(self):
    self.mv("deps/openssl/nodejs-openssl.cnf", ".")

    for f in [
        "deps/brotli",
        "deps/cares",
        "deps/openssl",
        "deps/zlib",
        "deps/v8/third_party/jinja2",
        "tools/inspector_protocol/jinja2",
    ]:
        self.rm(f, recursive=True)

    self.mkdir("deps/openssl")
    self.mv("nodejs-openssl.cnf", "deps/openssl")


def post_install(self):
    self.install_license("LICENSE")


# real test suite requires network acccess
def do_check(self):
    npath = self.chroot_cwd / "out/Release"
    nexe = npath / "node"
    self.do(nexe, "-e", "console.log('test')", wrksrc="out/Release")
    self.do(
        nexe,
        "-e",
        f"require('assert').equal(process.versions.node, '{pkgver}')",
        wrksrc="out/Release",
    )


@subpackage("nodejs-devel")
def _devel(self):
    return self.default_devel()
