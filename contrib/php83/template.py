pkgname = "php83"
pkgver = "8.3.6"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    # common parameters
    "--datadir=/usr/share/php83",
    "--datarootdir=/usr/share/php83",
    "--includedir=/usr/include",
    "--libdir=/usr/lib/php83",
    "--localstatedir=/var",
    "--mandir=/usr/share/man",
    "--prefix=/usr",
    "--program-prefix=",
    "--program-suffix=-83",
    "--sbindir=/usr/bin",
    "--sysconfdir=/etc/php83",
    "--with-config-file-path=/etc/php83",
    "--with-config-file-scan-dir=/etc/php83/conf.d",
    "--with-layout=GNU",
    # php-fpm
    "--enable-fpm",
    "--with-fpm-group=_php",
    "--with-fpm-user=_php",
    # extensions
    "--disable-all",
    "--enable-bcmath=shared",
    "--with-bz2=shared",
    "--enable-calendar=shared",
    "--enable-ctype=shared",
    "--with-curl=shared",
    "--enable-dom=shared",
    "--enable-exif=shared",
    "--with-ffi=shared",
    "--enable-fileinfo=shared",
    "--enable-filter=shared",
    "--enable-ftp=shared",
    "--enable-gd=shared",
    "--with-external-gd",
    "--with-gettext=shared",
    "--with-gmp=shared",
    "--with-iconv=shared",
    "--enable-intl=shared",
    "--with-libedit=shared",
    "--with-libxml",
    "--enable-mbstring=shared",
    "--with-mhash",
    "--enable-opcache=shared",
    "--with-openssl=shared",
    "--with-password-argon2",
    "--enable-pcntl=shared",
    "--enable-phar=shared",
    "--enable-posix=shared",
    "--enable-session=shared",
    "--enable-shmop=shared",
    "--enable-simplexml=shared",
    "--enable-soap=shared",
    "--enable-sockets=shared",
    "--with-sodium=shared",
    "--with-sqlite3=shared",
    "--enable-sysvmsg=shared",
    "--enable-sysvsem=shared",
    "--enable-sysvshm=shared",
    "--enable-tokenizer=shared",
    "--with-unixODBC=shared",
    "--enable-xml=shared",
    "--enable-xmlreader=shared",
    "--enable-xmlwriter=shared",
    "--with-xsl=shared",
    "--with-zip=shared",
    "--with-zlib=shared",
]
configure_gen = []
make_check_target = "test"
make_check_env = {
    "LANG": "",
    "LC_ALL": "",
    "NO_INTERACTION": "1",
    "REPORT_EXIT_STATUS": "1",
    "SKIP_IO_CAPTURE_TESTS": "1",
    "SKIP_ONLINE_TESTS": "1",
    "SKIP_PERF_SENSITIVE": "1",
    "SKIP_SLOW_TESTS": "1",
    "TEST_TIMEOUT": "10",
    "TZ": "",
}
hostmakedepends = [
    "automake",
    "bison",
    "libtool",
    "pkgconf",
]
makedepends = [
    "argon2-devel",
    "freetype-devel",
    "gettext-devel",
    "gmp-devel",
    "icu-devel",
    "libcurl-devel",
    "libedit-devel",
    "libffi-devel",
    "libgd-devel",
    "libjpeg-turbo-devel",
    "libsodium-devel",
    "libxml2-devel",
    "libxslt-devel",
    "libzip-devel",
    "oniguruma-devel",
    "openssl-devel",
    "sqlite-devel",
    "unixodbc-devel",
    "zlib-devel",
]
checkdepends = ["procps"]
pkgdesc = "HTML-embedded scripting language"
maintainer = "Renato Botelho do Couto <renato@netgate.com>"
license = "PHP-3.01"
url = "https://www.php.net"
source = f"{url}/distributions/php-{pkgver}.tar.gz"
sha256 = "39695f5bd107892e36fd2ed6b3d3a78140fd4b05d556d6c6531a921633cacb5f"


def post_patch(self):
    # Workaround issue with gettext tests
    self.cp(
        "ext/gettext/tests/locale/en_US.UTF-8",
        "ext/gettext/tests/locale/en_US",
        True,
    )
    # Remove tests that don't work
    for f in [
        # Obtained from Alpine
        "ext/iconv/tests/bug48147.phpt",
        "ext/iconv/tests/bug52211.phpt",
        "ext/iconv/tests/bug76249.phpt",
        "ext/iconv/tests/eucjp2iso2022jp.phpt",
        "ext/iconv/tests/iconv_mime_encode.phpt",
        "ext/opcache/tests/issue0115.phpt",
        "ext/opcache/tests/issue0149.phpt",
        "ext/pcntl/tests/pcntl_setpriority_error_linux.phpt",
        "ext/soap/tests/bug73037.phpt",
        "ext/soap/tests/server009.phpt",
        "ext/sockets/tests/bug63000.phpt",
        "sapi/fpm/tests/socket-ipv4-fallback.phpt",
        # Marked as XFAIL on PHP repo in March 2024
        "ext/openssl/tests/openssl_error_string_basic_openssl3.phpt",
        "ext/openssl/tests/openssl_private_decrypt_basic.phpt",
        # Broken and being discussed upstream
        # https://github.com/php/php-src/issues/11252
        "ext/gd/tests/bug43073.phpt",
        "ext/gd/tests/bug48732-mb.phpt",
        "ext/gd/tests/bug48732.phpt",
        "ext/gd/tests/bug48801-mb.phpt",
        "ext/gd/tests/bug48801.phpt",
        "ext/gd/tests/bug53504.phpt",
        "ext/gd/tests/bug65148.phpt",
        "ext/gd/tests/bug73272.phpt",
        # https://github.com/php/php-src/issues/13806
        "ext/openssl/tests/openssl_x509_parse_basic.phpt",
        # Under investigation
        "ext/gettext/tests/bug53251.phpt",
        "ext/gettext/tests/gettext_bind_textdomain_codeset-retval.phpt",
        "ext/gettext/tests/gettext_bindtextdomain-cwd.phpt",
        "ext/posix/tests/posix_errno_variation1.phpt",
        "ext/zip/tests/oo_encryption.phpt",
        "sapi/cli/tests/009.phpt",
        "sapi/cli/tests/012-2.phpt",
        "sapi/fpm/tests/bug77780-header-sent-error.phpt",
    ]:
        self.rm(f)


def init_install(self):
    self.make_install_args += [
        f"INSTALL_ROOT={self.chroot_destdir}",
    ]


def post_install(self):
    self.install_license("LICENSE")
    self.install_file("README.md", "usr/share/doc/php83")
    self.install_file(
        self.files_path / "sysusers.conf",
        "usr/lib/sysusers.d",
        name="php-fpm.conf",
    )
    self.install_service(self.files_path / "php-fpm")
    # default php-fpm config files
    self.mv(
        self.destdir / "etc/php83/php-fpm.conf.default",
        self.destdir / "etc/php83/php-fpm.conf",
    )
    self.install_file(self.files_path / "www.conf", "etc/php83/php-fpm.d")
    # these are unnecessary with apk backups
    self.rm(self.destdir / "etc/php83/php-fpm.d/*.default", glob=True)
    # extensions
    extcp = self.destdir / "etc/php83/conf.d"
    self.mkdir(extcp, parents=True)
    for f in (self.destdir / "usr/lib/php83/20230831/").glob("*.so"):
        extso = f.name.split("/")[-1]
        extn = extso.removesuffix(".so")
        with open(extcp / f"{extn}.ini", "w") as outf:
            if extn == "opcache":
                outf.write(f"zend_extension={extso}\n")
            else:
                outf.write(f"extension={extso}\n")


def _extension(extn, iif):
    @subpackage(f"php83-{extn}")
    def _ext(self):
        self.pkgdesc = f"{pkgdesc} ({extn} extension)"

        if iif:
            self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}"]

        return [
            f"etc/php83/conf.d/{extn}.ini",
            f"usr/lib/php83/20230831/{extn}.so",
        ]


# extensions
for _extn, _iif in [
    ("bcmath", False),
    ("bz2", False),
    ("calendar", False),
    ("ctype", True),
    ("curl", False),
    ("dom", True),
    ("exif", False),
    ("ffi", False),
    ("fileinfo", True),
    ("filter", True),
    ("ftp", False),
    ("gd", False),
    ("gettext", False),
    ("gmp", False),
    ("iconv", True),
    ("intl", False),
    ("mbstring", False),
    ("odbc", False),
    ("opcache", True),
    ("openssl", False),
    ("pcntl", False),
    ("phar", True),
    ("posix", True),
    ("readline", False),
    ("session", True),
    ("shmop", False),
    ("simplexml", True),
    ("soap", False),
    ("sockets", False),
    ("sodium", False),
    ("sqlite3", True),
    ("sysvmsg", False),
    ("sysvsem", False),
    ("sysvshm", False),
    ("tokenizer", True),
    ("xml", True),
    ("xmlreader", True),
    ("xmlwriter", True),
    ("xsl", False),
    ("zip", False),
    ("zlib", False),
]:
    _extension(_extn, _iif)


@subpackage("php83-devel")
def _devel(self):
    return self.default_devel(
        extra=[
            "usr/bin/phpize-83",
            "usr/lib/php83/build",
        ]
    )
