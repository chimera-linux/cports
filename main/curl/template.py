pkgname = "curl"
pkgver = "8.18.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-optimize",
    "--enable-ares",
    "--enable-httpsrr",
    "--enable-ipv6",
    "--enable-threaded-resolver",
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
hostmakedepends = ["automake", "pkgconf", "perl", "mandoc", "slibtool"]
makedepends = [
    "c-ares-devel",
    "libidn2-devel",
    "libpsl-devel",
    "libssh2-devel",
    "nghttp2-devel",
    "nghttp3-devel",
    "openssl3-devel",
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
license = "MIT"
url = "https://curl.haxx.se"
source = f"{url}/download/curl-{pkgver}.tar.xz"
sha256 = "40df79166e74aa20149365e11ee4c798a46ad57c34e4f68fd13100e2c9a91946"
hardening = ["vis", "!cfi"]


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
    # 1510 consistently fails when run with other tests (parallelism?)
    # but works just fine when run on its own
    self.make_check_env["TFLAGS"] = f"-j{self.make_jobs * 7} !1510"


@subpackage("curl-libs")
def _(self):
    self.pkgdesc = "Multiprotocol file transfer library"
    self.renames = ["libcurl"]

    return self.default_libs()


@subpackage("curl-devel")
def _(self):
    self.depends += makedepends
    self.pkgdesc = "Multiprotocol file transfer library"
    self.renames = ["libcurl-devel"]

    return self.default_devel()
