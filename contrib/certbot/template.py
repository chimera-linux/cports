pkgname = "certbot"
pkgver = "2.11.0"
pkgrel = 1
build_wrksrc = "certbot"
build_style = "python_pep517"
_plugins = [
    "certbot-apache",
    "certbot-dns-cloudflare",
    "certbot-dns-digitalocean",
    "certbot-dns-dnsimple",
    "certbot-dns-dnsmadeeasy",
    "certbot-dns-gehirn",
    "certbot-dns-linode",
    "certbot-dns-luadns",
    "certbot-dns-nsone",
    "certbot-dns-ovh",
    "certbot-dns-rfc2136",
    "certbot-dns-route53",
    "certbot-dns-sakuracloud",
    "certbot-nginx",
]
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = [
    "python-acme",
    "python-configargparse",
    "python-configobj",
    "python-cryptography",
    "python-distro",
    "python-josepy",
    "python-parsedatetime",
]
_plugindeps = [
    "python-boto3",
    "python-botocore",
    "python-cloudflare",
    "python-digitalocean",
    "python-dnspython",
]
checkdepends = ["python-pytest-xdist"] + depends + _plugindeps
pkgdesc = "Tool to obtain certs from Let's Encrypt"
maintainer = "Duncan Bellamy <dunk@denkimushi.com>"
license = "Apache-2.0 AND MIT"
url = "https://github.com/certbot/certbot"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "93764a18e0b19fe5fc7471a02a2df1937c40eb65c86b3f9ea11b40416c1541dc"


def post_build(self):
    for plugin in _plugins:
        self.do(
            "python",
            "-m",
            "build",
            "--wheel",
            "--no-isolation",
            f"../{plugin}",
        )


def init_check(self):
    self.make_check_args += [
        f"--numprocesses={self.make_jobs}",
        "--dist=worksteal",
    ]


def post_install(self):
    for plugin in _plugins:
        self.do(
            "python",
            "-m",
            "installer",
            "--compile-bytecode",
            "0",
            "--destdir",
            self.chroot_destdir,
            f"../{plugin}/dist/{plugin.replace('-', '_')}-{pkgver}-py3-none-any.whl",
        )
    self.install_license("LICENSE.txt")


def _genmod(pname, pdesc):
    @subpackage(f"certbot-{pname}")
    def _plug(self):
        self.pkgdesc = f"{pdesc} plugin for certbot"
        self.depends += [f"{pkgname}={pkgver}-r{pkgrel}"]
        match pname:
            case "dns-cloudflare":
                self.depends += ["python-cloudflare"]
            case "dns-digitalocean":
                self.depends += ["python-digitalocean"]
            case "dns-rfc2136":
                self.depends += ["python-dnspython"]
            case "dns-route53":
                self.depends += ["python-boto3", "python-botocore"]
            case "nginx":
                self.depends += ["python-openssl", "python-pyparsing"]
                self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}", "nginx"]

        return [
            f"usr/lib/python*/site-packages/certbot_{pname.replace('-', '_')}*"
        ]


for _plugin, _desc in [
    ("apache", "Apache"),
    ("dns-cloudflare", "Cloudflare dns authenticator"),
    ("dns-digitalocean", "Digitalocean dns authenticator"),
    ("dns-dnsimple", "DNSimple dns authenticator"),
    ("dns-dnsmadeeasy", "DNS made easy dns authenticator"),
    ("dns-gehirn", "Gehirn infrastructure service dns authenticator"),
    ("dns-linode", "Linode dns authenticator"),
    ("dns-luadns", "Luadns authenticator"),
    ("dns-nsone", "NS1 dns authenticator"),
    ("dns-ovh", "OVH dns authenticator"),
    ("dns-rfc2136", "RFC 2136 dns authenticator"),
    ("dns-route53", "Amazon web services route 53 dns authenticator"),
    ("dns-sakuracloud", "Sakura cloud dns authenticator"),
    ("nginx", "Nginx"),
]:
    _genmod(_plugin, _desc)
