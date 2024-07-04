pkgname = "nginx"
pkgver = "1.26.1"
pkgrel = 2
build_style = "configure"
configure_args = [
    "--prefix=/var/lib/nginx",
    "--user=_nginx",
    "--group=_nginx",
    "--with-file-aio",
    "--conf-path=/etc/nginx/nginx.conf",
    "--error-log-path=/var/log/nginx/error.log",
    "--http-log-path=/var/log/nginx/access.log",
    "--lock-path=/run/nginx/nginx.lock",
    "--modules-path=/usr/lib/nginx/modules",
    "--pid-path=/run/nginx/nginx.pid",
    "--sbin-path=/usr/bin/nginx",
    "--http-client-body-temp-path=/var/lib/nginx/tmp/client_body_temp",
    "--http-fastcgi-temp-path=/var/lib/nginx/tmp/fastcgi_temp",
    "--http-proxy-temp-path=/var/lib/nginx/tmp/proxy_temp",
    "--http-scgi-temp-path=/var/lib/nginx/tmp/scgi_temp",
    "--http-uwsgi-temp-path=/var/lib/nginx/tmp/uwsgi_temp",
    "--with-compat",
    "--with-http_addition_module",
    "--with-http_auth_request_module",
    "--with-http_dav_module",
    "--with-http_flv_module",
    # "--with-http_geoip_module=dynamic", TODO
    "--with-http_gunzip_module",
    "--with-http_gzip_static_module",
    "--with-http_image_filter_module=dynamic",
    "--with-http_mp4_module",
    "--with-http_perl_module=dynamic",
    "--with-http_random_index_module",
    "--with-http_realip_module",
    "--with-http_secure_link_module",
    "--with-http_slice_module",
    "--with-http_ssl_module",
    "--with-http_stub_status_module",
    "--with-http_sub_module",
    "--with-http_v2_module",
    "--with-http_v3_module",
    "--with-http_xslt_module=dynamic",
    "--with-mail=dynamic",
    "--with-mail_ssl_module",
    "--with-pcre",
    "--with-pcre-jit",
    "--with-perl_modules_path=/usr/lib/perl5/vendor_perl",
    "--with-stream=dynamic",
    # "--with-stream_geoip_module=dynamic", TODO
    "--with-stream_realip_module",
    "--with-stream_ssl_module",
    "--with-stream_ssl_preread_module",
    "--with-threads",
    "--without-mail_imap_module",
    "--without-mail_pop3_module",
    "--without-mail_smtp_module",
]
make_dir = "."
# cross will need both sets of dependencies in the future
hostmakedepends = [
    "libgd-devel",
    "libxml2-devel",
    "libxslt-devel",
    "linux-headers",
    "openssl-devel",
    "pcre2-devel",
    "perl",
    "zlib-ng-compat-devel",
]
makedepends = list(hostmakedepends)
checkdepends = [
    "ca-certificates",
    "ffmpeg",
    "libgd-progs",
    "perl-io-socket-ssl",
    "perl-net-ssleay",
]
pkgdesc = "Advanced load balancer, web server, and reverse proxy"
maintainer = "Renato Botelho do Couto <renato@netgate.com>"
license = "BSD-2-Clause"
url = "https://nginx.org"
_test_hash = "0b5ec15c62ed"
source = [
    f"https://nginx.org/download/{pkgname}-{pkgver}.tar.gz",
    f"https://hg.nginx.org/nginx-tests/archive/{_test_hash}.tar.gz",
]
source_paths = [".", "nginx-tests"]
sha256 = [
    "f9187468ff2eb159260bfd53867c25ff8e334726237acf227b9e870e53d3e36b",
    "c9b464e6f9cc129eade5d3068c168bf598513d346799483c73cd18c107859d38",
]
# needs a lot more work
options = ["!cross"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_file("README", "usr/share/doc/nginx")
    self.install_man("man/nginx.8")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_service(self.files_path / "nginx")
    # must be present in main package
    self.install_dir("usr/lib/nginx/modules", empty=True)
    # better default configs, mostly adapted from alpine
    self.uninstall("etc/nginx/nginx.conf")
    self.install_file(self.files_path / "nginx.conf", "etc/nginx")
    self.install_file(self.files_path / "default.conf", "etc/nginx/http.d")
    self.install_file(self.files_path / "stream.conf", "etc/nginx/conf.d")
    # needed for relative module loads
    self.install_link("var/lib/nginx/modules", "../../../usr/lib/nginx/modules")
    # remove old charset maps
    self.uninstall("etc/nginx/koi-*", glob=True)
    self.uninstall("etc/nginx/win-utf")
    # these interfere with tmpfiles ownership and are not used anyway
    self.uninstall("var/lib/nginx/html")
    # these are unnecessary with apk backups
    self.uninstall("etc/nginx/*.default", glob=True)


def do_check(self):
    with self.pushd("nginx-tests"):
        self.do(
            "prove",
            f"--jobs={self.make_jobs}",
            ".",
            env={"TEST_NGINX_BINARY": "../objs/nginx"},
        )


def _module(modn, eiif):
    @subpackage(f"nginx-module-{modn}")
    def _mod(self):
        self.pkgdesc = f"{pkgdesc} ({modn} module)"

        modso = f"modules/ngx_{modn}_module.so"
        ret = [f"usr/lib/nginx/{modso}"]

        if eiif is not False:
            iif = [f"{pkgname}={pkgver}-r{pkgrel}"]
            if eiif:
                iif += [eiif]
            self.install_if = iif

        # extra files
        if modn == "http_perl":
            ret += ["usr/lib/perl5"]
        elif modn == "stream":
            ret += ["etc/nginx/conf.d/stream.conf"]

        def do_inst():
            # module loader
            modcp = self.destdir / "etc/nginx/modules"
            self.mkdir(modcp, parents=True)
            with open(modcp / f"000_{modn}.conf", "w") as outf:
                outf.write(f'load_module "{modso}";\n')
            # other stuff
            for pat in ret:
                self.take(pat)

        return do_inst


# dynamic modules shipped with nginx
for _modn, _iif in [
    ("http_image_filter", False),
    ("http_perl", "perl"),
    ("http_xslt_filter", None),
    ("mail", False),
    ("stream", None),
]:
    _module(_modn, _iif)
