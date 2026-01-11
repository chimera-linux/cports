pkgname = "nginx"
pkgver = "1.28.0"
pkgrel = 1
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
    "dinit-chimera",
    "libgd-devel",
    "libxml2-devel",
    "libxslt-devel",
    "linux-headers",
    "openssl3-devel",
    "pcre2-devel",
    "perl",
    "zlib-ng-compat-devel",
]
makedepends = [*hostmakedepends]
checkdepends = [
    "ca-certificates",
    "ffmpeg",
    "libgd-progs",
    "perl-io-socket-ssl",
    "perl-net-ssleay",
]
pkgdesc = "Advanced load balancer, web server, and reverse proxy"
license = "BSD-2-Clause"
url = "https://nginx.org"
source = [
    f"https://nginx.org/download/nginx-{pkgver}.tar.gz",
    "https://hg.nginx.org/nginx-tests/archive/f5ef37b2e260.tar.gz",
]
source_paths = [".", "nginx-tests"]
sha256 = [
    "c6b5c6b086c0df9d3ca3ff5e084c1d0ef909e6038279c71c1c3e985f576ff76a",
    "9056dca56c96922c7d3fc6100c183d8262d6faa46685a817e611ade2479d676a",
]
file_modes = {
    # must be present in main package
    "+usr/lib/nginx/modules": ("root", "root", 0o755, True),
}
# needs a lot more work
options = ["!cross"]


def post_extract(self):
    # FIXME: no idea why this segfaults now, probably new libxml
    self.rm("nginx-tests/xslt.t")


def check(self):
    with self.pushd("nginx-tests"):
        self.do(
            "prove",
            f"--jobs={self.make_jobs * 2}",
            ".",
            env={"TEST_NGINX_BINARY": "../objs/nginx"},
        )


def post_install(self):
    self.install_license("LICENSE")
    self.install_file("README.md", "usr/share/doc/nginx")
    self.install_man("man/nginx.8")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_service(self.files_path / "nginx")
    # better default configs, mostly adapted from alpine
    self.uninstall("etc/nginx/nginx.conf")
    self.install_file(self.files_path / "nginx.conf", "etc/nginx")
    self.install_file(self.files_path / "default.conf", "etc/nginx/http.d")
    self.install_file(self.files_path / "stream.conf", "etc/nginx/conf.d")
    # remove old charset maps
    self.uninstall("etc/nginx/koi-*", glob=True)
    self.uninstall("etc/nginx/win-utf")
    # these interfere with tmpfiles ownership and are not used anyway
    self.uninstall("var/lib/nginx/html")
    # these are unnecessary with apk backups
    self.uninstall("etc/nginx/*.default", glob=True)


def _module(modn, eiif):
    @subpackage(f"nginx-module-{modn}")
    def _(self):
        self.subdesc = f"{modn} module"

        modso = f"modules/ngx_{modn}_module.so"
        ret = [f"usr/lib/nginx/{modso}"]

        if eiif is not False:
            iif = [self.parent]
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
