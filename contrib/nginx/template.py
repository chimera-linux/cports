pkgname = "nginx"
pkgver = "1.24.0"
pkgrel = 0
build_style = "configure"
configure_args = [
    "--prefix=/etc/nginx",
    "--user=_nginx",
    "--group=www-data",
    "--with-file-aio",
    "--conf-path=/etc/nginx/nginx.conf",
    "--error-log-path=/var/log/nginx/error.log",
    "--http-log-path=/var/log/nginx/access.log",
    "--lock-path=/run/nginx/nginx.lock",
    "--modules-path=/usr/libexec/nginx",
    "--pid-path=/run/nginx/nginx.pid",
    "--sbin-path=/usr/bin/nginx",
    "--http-client-body-temp-path=/var/tmp/nginx/client_body_temp",
    "--http-fastcgi-temp-path=/var/tmp/nginx/fastcgi_temp",
    "--http-proxy-temp-path=/var/tmp/nginx/proxy_temp",
    "--http-scgi-temp-path=/var/tmp/nginx/scgi_temp",
    "--http-uwsgi-temp-path=/var/tmp/nginx/uwsgi_temp",
    "--with-compat",
    "--with-http_addition_module",
    "--with-http_auth_request_module",
    "--with-http_dav_module",
    "--with-http_flv_module",
    "--with-http_gunzip_module",
    "--with-http_gzip_static_module",
    "--with-http_mp4_module",
    "--with-http_random_index_module",
    "--with-http_realip_module",
    "--with-http_secure_link_module",
    "--with-http_slice_module",
    "--with-http_ssl_module",
    "--with-http_stub_status_module",
    "--with-http_sub_module",
    "--with-http_v2_module",
    "--with-http_xslt_module",
    "--with-mail=dynamic",
    "--with-mail_ssl_module",
    "--with-pcre",
    "--with-stream=dynamic",
    "--with-stream_realip_module",
    "--with-stream_ssl_module",
    "--with-stream_ssl_preread_module",
    "--with-threads",
    "--without-mail_imap_module",
    "--without-mail_pop3_module",
    "--without-mail_smtp_module",
]
make_dir = "."
hostmakedepends = ["linux-headers"]
makedepends = [
    "libgd-devel",
    "libxml2-devel",
    "libxslt-devel",
    "openssl-devel",
    "pcre2-devel",
    "zlib-devel",
]
checkdepends = [
    "ca-certificates",
    "libgd-progs",
    "perl-io-socket-ssl",
    "perl-net-ssleay",
]
pkgdesc = "Robust and small WWW server"
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
    "77a2541637b92a621e3ee76776c8b7b40cf6d707e69ba53a940283e30ff2f55d",
    "c9b464e6f9cc129eade5d3068c168bf598513d346799483c73cd18c107859d38",
]


def post_install(self):
    self.install_license("LICENSE")
    self.install_man("man/nginx.8")
    self.install_file(
        self.files_path / "sysusers.conf",
        "usr/lib/sysusers.d",
        name="nginx.conf",
    )
    self.install_file(
        self.files_path / "tmpfiles.conf",
        "usr/lib/tmpfiles.d",
        name="nginx.conf",
    )
    self.install_service(self.files_path / "nginx")


def do_check(self):
    with self.pushd("nginx-tests"):
        self.do(
            "prove",
            f"--jobs={self.make_jobs}",
            ".",
            env={"TEST_NGINX_BINARY": "../objs/nginx"},
        )
