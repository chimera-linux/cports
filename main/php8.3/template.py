pkgname = "php8.3"
_majver = "8.3"
pkgver = f"{_majver}.16"
pkgrel = 0
_apiver = "20230831"
build_style = "gnu_configure"
configure_args = [
    # common parameters
    f"--datadir=/usr/share/php{_majver}",
    f"--datarootdir=/usr/share/php{_majver}",
    f"--includedir=/usr/include/php{_majver}",
    f"--libdir=/usr/lib/php{_majver}",
    "--program-prefix=",
    f"--program-suffix={_majver}",
    f"--sysconfdir=/etc/php{_majver}",
    f"--with-config-file-path=/etc/php{_majver}",
    f"--with-config-file-scan-dir=/etc/php{_majver}/conf.d",
    "--with-layout=GNU",
    # php-fpm
    "--enable-fpm",
    "--with-fpm-group=_php",
    "--with-fpm-user=_php",
    # extensions
    "--disable-all",
    "--enable-bcmath=shared",
    "--enable-calendar=shared",
    "--enable-ctype=shared",
    "--enable-dom=shared",
    "--enable-exif=shared",
    "--enable-fileinfo=shared",
    "--enable-filter=shared",
    "--enable-ftp=shared",
    "--enable-gd=shared",
    "--enable-intl=shared",
    "--enable-mbstring=shared",
    "--enable-opcache=shared",
    "--enable-pcntl=shared",
    "--enable-pdo=shared",
    "--enable-phar=shared",
    "--enable-posix=shared",
    "--enable-session=shared",
    "--enable-shmop=shared",
    "--enable-simplexml=shared",
    "--enable-soap=shared",
    "--enable-sockets=shared",
    "--enable-sysvmsg=shared",
    "--enable-sysvsem=shared",
    "--enable-sysvshm=shared",
    "--enable-tokenizer=shared",
    "--enable-xml=shared",
    "--enable-xmlreader=shared",
    "--enable-xmlwriter=shared",
    "--with-bz2=shared",
    "--with-curl=shared",
    "--with-external-gd",
    "--with-ffi=shared",
    "--with-gettext=shared",
    "--with-gmp=shared",
    "--with-iconv=shared",
    "--with-ldap-sasl",
    "--with-ldap=shared",
    "--with-libedit=shared",
    "--with-libxml",
    "--with-mhash",
    "--with-openssl=shared",
    "--with-password-argon2",
    "--with-pdo-sqlite=shared",
    "--with-pear",
    "--with-sodium=shared",
    "--with-sqlite3=shared",
    "--with-unixODBC=shared",
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
    "curl-devel",
    "libedit-devel",
    "libffi-devel",
    "libgd-devel",
    "libjpeg-turbo-devel",
    "libsodium-devel",
    "libxml2-devel",
    "libxslt-devel",
    "libzip-devel",
    "oniguruma-devel",
    "openldap-devel",
    "openssl-devel",
    "sqlite-devel",
    "unixodbc-devel",
    "zlib-ng-compat-devel",
]
checkdepends = ["procps"]
depends = ["php-common"]
provides = ["php-runtime"]
pkgdesc = "HTML-embedded scripting language"
maintainer = "Renato Botelho do Couto <renato@netgate.com>"
license = "PHP-3.01"
url = "https://www.php.net"
source = f"{url}/distributions/php-{pkgver}.tar.gz"
sha256 = "61441627dca50cf0173e3f054ffe8c4f5db6552555c43cab87a8ecacfd201c7e"


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
        # aarch64; all related to chunked encoding?
        "ext/soap/tests/bug47021.phpt",
        "ext/standard/tests/filters/chunked_001.phpt",
        "ext/standard/tests/http/bug47021.phpt",
        "ext/standard/tests/http/bug80256.phpt",
        # ppc64le; all related to fibers?
        "Zend/tests/fibers/no-switch-force-close-finally.phpt",
        "Zend/tests/fibers/suspend-in-force-close-fiber-after-shutdown.phpt",
        "Zend/tests/fibers/throw-in-multiple-destroyed-fibers-after-shutdown.phpt",
        "Zend/tests/gh9916-009.phpt",
        # Under investigation
        "ext/gettext/tests/bug53251.phpt",
        "ext/gettext/tests/gettext_bind_textdomain_codeset-retval.phpt",
        "ext/gettext/tests/gettext_bindtextdomain-cwd.phpt",
        "ext/posix/tests/posix_errno_variation1.phpt",
        "ext/standard/tests/http/gh16810.phpt",
        "ext/zip/tests/oo_encryption.phpt",
        "sapi/cli/tests/009.phpt",
        "sapi/cli/tests/012-2.phpt",
        "sapi/fpm/tests/bug77780-header-sent-error.phpt",
        # fails with new xml libs
        "ext/dom/tests/DOMDocument_loadHTMLfile_error1.phpt",
        "ext/dom/tests/DOMDocument_loadXML_error2_gte2_12.phpt",
        "ext/dom/tests/DOMDocument_load_error2_gte2_12.phpt",
        "ext/dom/tests/DOMDocument_relaxNGValidate_error2.phpt",
        "ext/dom/tests/DOMDocument_saveHTMLFile_basic.phpt",
        "ext/dom/tests/DOMDocument_saveHTMLFile_formatOutput.phpt",
        "ext/dom/tests/DOMDocument_schemaValidate_error5.phpt",
        "ext/dom/tests/DOMElement_insertAdjacentText.phpt",
        "ext/dom/tests/DOMEntityReference_predefined_free.phpt",
        "ext/dom/tests/dom_create_element.phpt",
        "ext/libxml/tests/bug61367-read_2.phpt",
        "ext/libxml/tests/libxml_disable_entity_loader_2.phpt",
        "ext/libxml/tests/libxml_set_external_entity_loader_variation1.phpt",
        "ext/simplexml/tests/bug63575.phpt",
        "ext/simplexml/tests/bug76712.phpt",
        "ext/simplexml/tests/bug79971_1.phpt",
        "ext/soap/tests/bug69668.phpt",
        "ext/soap/tests/bugs/bug42151.phpt",
        # probably fails because of zlib-ng-compat
        "ext/zlib/tests/bug48725.phpt",
        # most of these try connect to an ldap server and wait for timeout then autoskip
        "ext/ldap/tests/*.phpt",
        # icu 76
        "ext/intl/tests/bug62070_3.phpt",
        "ext/intl/tests/collator_get_sort_key_variant7.phpt",
        "ext/intl/tests/timezone_IDforWindowsID_basic2.phpt",
    ]:
        self.rm(f, glob=True)


def init_check(self):
    # injected via patch
    # also seem to hang sometimes with too many jobs
    self.make_check_args += [f"PHP_RUN_TESTS_ARGS=-j{min(6, self.make_jobs)}"]


def init_install(self):
    self.make_install_args += [
        f"INSTALL_ROOT={self.chroot_destdir}",
    ]


def post_install(self):
    self.install_license("LICENSE")
    self.install_file("README.md", f"usr/share/doc/php{_majver}")
    self.install_service(self.files_path / f"php-fpm{_majver}")
    # default php-fpm config files
    self.rename(f"etc/php{_majver}/php-fpm.conf.default", "php-fpm.conf")
    for f in ["pear", "peardev", "pecl"]:
        self.rename(f"usr/bin/{f}", f"{f}{_majver}")
    self.install_file(
        self.files_path / "www.conf", f"etc/php{_majver}/php-fpm.d"
    )
    # these are unnecessary with apk backups
    self.uninstall(f"etc/php{_majver}/php-fpm.d/*.default", glob=True)
    # extensions
    extcp = self.destdir / f"etc/php{_majver}/conf.d"
    self.mkdir(extcp, parents=True)
    for f in (self.destdir / f"usr/lib/php{_majver}" / _apiver).glob("*.so"):
        extso = f.name.split("/")[-1]
        extn = extso.removesuffix(".so")
        with open(extcp / f"{extn}.ini", "w") as outf:
            if extn == "opcache":
                outf.write(f"zend_extension={extso}\n")
            else:
                outf.write(f"extension={extso}\n")
    # remove temporary files/dirs that shouldn't be part of package
    for f in [
        ".channels",
        ".depdb",
        ".depdblock",
        ".filemap",
        ".lock",
        f"usr/share/php{_majver}/pear/.channels",
        f"usr/share/php{_majver}/pear/.filemap",
        f"usr/share/php{_majver}/pear/.lock",
        f"usr/share/php{_majver}/pear/.registry",
        f"usr/share/php{_majver}/pear/test",
    ]:
        self.uninstall(f)


@subpackage(pkgname, alternative="php")
def _(self):
    # this is the default version
    self.provider_priority = 100
    return [
        f"@usr/lib/dinit.d/php-fpm=>php-fpm{_majver}",
        f"@usr/bin/pear=>pear{_majver}",
        f"@usr/bin/peardev=>peardev{_majver}",
        f"@usr/bin/pecl=>pecl{_majver}",
        f"@usr/bin/phar=>phar{_majver}",
        f"@usr/bin/phar.phar=>phar{_majver}.phar",
        f"@usr/bin/php=>php{_majver}",
        f"@usr/bin/php-cgi=>php-cgi{_majver}",
        f"@usr/bin/php-config=>php-config{_majver}",
        f"@usr/bin/php-fpm=>php-fpm{_majver}",
        f"@usr/bin/phpdbg=>phpdbg{_majver}",
    ]


def _extension(extn, iif):
    @subpackage(f"php{_majver}-{extn}")
    def _(self):
        self.subdesc = f"{extn} extension"
        self.depends += [self.parent]

        if iif:
            self.install_if = [self.parent]

        return [
            f"etc/php{_majver}/conf.d/{extn}.ini",
            f"usr/lib/php{_majver}/{_apiver}/{extn}.so",
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
    ("ldap", False),
    ("mbstring", False),
    ("odbc", False),
    ("opcache", True),
    ("openssl", False),
    ("pcntl", False),
    ("pdo", True),
    ("pdo_sqlite", True),
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


@subpackage(f"php{_majver}-pear")
def _(self):
    self.pkgdesc = f"PHP{_majver} Extension and Application Repository"
    self.depends = [self.parent, f"{pkgname}-xml"]
    self.install_if = [self.parent]

    return [
        f"etc/php{_majver}/pear.conf",
        f"usr/bin/pear{_majver}",
        f"usr/bin/peardev{_majver}",
        f"usr/bin/pecl{_majver}",
        f"usr/share/php{_majver}/pear",
    ]


@subpackage(f"php{_majver}-devel")
def _(self):
    self.depends += [self.parent]

    return self.default_devel(
        extra=[
            f"usr/bin/phpize{_majver}",
            f"usr/lib/php{_majver}/build",
        ]
    )
