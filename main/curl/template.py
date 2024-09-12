pkgname = "curl"
pkgver = "8.10.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-optimize",
    "--enable-ares",
    "--enable-ipv6",
    "--enable-threaded-resolver",
    "--enable-threads",
    "--enable-websockets",
    "--with-ca-bundle=/etc/ssl/certs/ca-certificates.crt",
    "--with-fish-functions-dir=/usr/share/fish/vendor_completions.d",
    "--with-libidn2",
    "--with-libpsl",
    "--with-libssh2",
    "--with-nghttp2",
    "--with-nghttp3",
    "--with-openssl-quic",
    "--with-ssl",
    "--with-zlib",
    "--with-zsh-functions-dir=/usr/share/zsh/site-functions/",
    "--with-zstd",
    "ac_cv_path_NROFF=/usr/bin/mandoc",
    "ac_cv_sizeof_off_t=8",
]
hostmakedepends = ["pkgconf", "perl", "mandoc"]
makedepends = [
    "c-ares-devel",
    "libidn2-devel",
    "libpsl-devel",
    "libssh2-devel",
    "nghttp2-devel",
    "nghttp3-devel",
    "openssl-devel",
    "zlib-ng-compat-devel",
    "zstd-devel",
]
checkdepends = [
    "nghttp2-progs",
    # FIXME: probably caused by weird config shenanigans
    # "openssh",
    "python",
]
depends = ["ca-certificates"]
pkgdesc = "Command line tool for transferring data with URL syntax"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://curl.haxx.se"
source = f"{url}/download/curl-{pkgver}.tar.xz"
sha256 = "e6b142f0e85e954759d37e26a3627e2278137595be80e3a860c4353e4335e5a0"
hardening = ["vis", "!cfi"]
# workaround for test 1119
exec_wrappers = [("/usr/bin/clang-cpp", "cpp")]


def post_install(self):
    self.install_license("COPYING")

    # patch curl-config for cross
    if not self.profile().cross:
        return

    with open(self.destdir / "usr/bin/curl-config") as inf:
        with open(self.destdir / "usr/bin/curl-config.new", "w") as outf:
            for ln in inf:
                ln = ln.replace(f"-L{self.profile().sysroot / 'usr/lib'} ", "")
                ln = ln.replace(f"{self.profile().triplet}-", "")
                outf.write(ln)

    self.rename("usr/bin/curl-config.new", "curl-config")
    self.chmod(self.destdir / "usr/bin/curl-config", 0o755)


def init_check(self):
    # upstream recommends cpucores*7 as a good starting point
    self.make_check_env["TFLAGS"] = f"-j{self.make_jobs * 7}"


@subpackage("libcurl")
def _(self):
    self.pkgdesc = "Multiprotocol file transfer library"

    return self.default_libs()


@subpackage("libcurl-devel")
def _(self):
    self.depends += makedepends
    self.pkgdesc = "Multiprotocol file transfer library"

    return self.default_devel()


configure_gen = []
