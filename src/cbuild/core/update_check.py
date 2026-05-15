# the logic here is largely adapted from xbps-src, since writing this stuff
# from scratch is a pain; it is adapted to use less cursed regexes than PCRE
# (mainly having verbose regex really helps readability) and allows for custom
# hooks inside update.py files

import builtins
import importlib
import importlib.util
import urllib.request as ureq
import fnmatch
import time
import gzip
import io
import re

from cbuild.apk import cli as apkcli


# implements version sorting as in gnu sort(1) version sort
def _get_verkey():
    import functools

    def _digind(s, f):
        for i, c in enumerate(s):
            if f(c):
                return i

        return len(s)

    def _scmp(a, b):
        clen = min(len(a), len(b))
        a1, a2 = a[:clen], a[clen:]
        b1, b2 = b[:clen], b[clen:]
        # compare the common part
        for c1, c2 in zip(a1, b1):
            if c1 == "~" or (c1.isalpha() and not c2.isalpha()):
                return -1
            if c1 != c2:
                if c1 < c2:
                    return -1
                else:
                    return 1
        # remainders
        if a2.startswith("~"):
            return -1
        if a2 == b2:
            return 0
        elif a2 < b2:
            return -1
        else:
            return 1

    def _getstrs(v):
        dp = _digind(v, lambda c: c.isdigit())
        s1 = v[:dp]
        v = v[dp:]
        ndp = _digind(v, lambda c: not c.isdigit())
        d1 = v[:ndp]
        return s1, int(d1) if len(d1) > 0 else 0, v[ndp:]

    def _vcmp(a, b):
        while len(a) > 0 or len(b) > 0:
            nd1, d1, a = _getstrs(a)
            nd2, d2, b = _getstrs(b)
            # compare non-digit part
            if nd1 != nd2:
                return _scmp(nd1, nd2)
            # compare digit part
            dd = d1 - d2
            if dd:
                return dd
        # equal strings
        return 0

    return functools.cmp_to_key(_vcmp)


_ver_conv = _get_verkey()


class UpdateCheck:
    def __init__(self, tmpl, verbose):
        self.verbose = verbose
        self._urlcache = {}
        self.template = tmpl
        self.url = None
        self.pkgname = tmpl.pkgname
        self.pkgver = tmpl.pkgver
        self.single_directory = False
        self.pattern = None
        self.group = None
        self.vdprefix = None
        self.vdsuffix = None
        self.ignore = []

    def _fetch(self, u):
        if u in self._urlcache:
            return False

        req = ureq.Request(
            u,
            None,
            {
                "User-Agent": "cbuild-update-check/4.20.69",
                "Accept-Encoding": "gzip",
            },
        )
        try:
            f = ureq.urlopen(req, None, 10)
            if f.info().get("Content-Encoding") == "gzip":
                resp = gzip.GzipFile(fileobj=io.BytesIO(f.read())).read()
            else:
                resp = f.read()
            ret = resp.decode("utf-8", "ignore")
        except Exception:
            return None

        self._urlcache[u] = True

        if len(ret) == 0:
            return None

        return ret

    def collect_sources(self):
        if isinstance(self.url, str):
            return [self.url]
        elif self.url:
            return self.url

        ret = []

        urls = []
        # collect urls
        for s in self.template.source:
            if s.startswith("!"):
                s = s[1:]
            bkt = s.rfind(">")
            bsl = s.rfind("/")
            if bkt > bsl:
                s = s[0:bkt]
            urls.append(s)

        for u in urls:
            if "ftp.gnome.org" in u:
                break
        else:
            ret.append(self.template.url)

        for u in urls:
            m = re.match(r"(.+)/[^/]+", u)
            if m:
                u = m[1]
            ret.append(u + "/")

        return ret

    def expand_source(self, url):
        ret = [url]

        if self.verbose:
            print(f"Adding '{url}' for version check...")

        if self.single_directory:
            return ret

        if (
            "chimera-linux.org" in url
            or ".voidlinux." in url
            or "sourceforge.net/sourceforge" in url
            or "launchpad.net" in url
            or "cpan." in url
            or "pythonhosted.org" in url
            or "github.com" in url
            or "//gitlab." in url
            or "bitbucket.org" in url
            or "ftp.gnome.org" in url
            or "archive.xfce.org" in url
            or "kernel.org/pub/linux/kernel/" in url
            or "cran.r-project.org/src/contrib" in url
            or "rubygems.org" in url
            or "crates.io" in url
            or "codeberg.org" in url
            or "hg.sr.ht" in url
            or "git.sr.ht" in url
            or "pagure.io" in url
        ):
            return ret

        if self.vdprefix:
            vdpfx = self.vdprefix
        else:
            vdpfx = rf"|v|{re.escape(self.pkgname)}"

        if self.vdsuffix:
            vdsfx = self.vdsuffix
        else:
            vdsfx = r"|\.x"

        rxm = re.compile(
            rf"""
            ^[^/]+// # scheme
            [^/]+(/.+)?/ # path
            ({vdpfx})
            (?=
                [-_.0-9]*[0-9](?<!
                    {re.escape(self.pkgname)}
                )({vdsfx})/
            )
        """,
            re.VERBOSE,
        )

        m = re.match(rxm, url)
        if not m:
            return ret

        tsl = m[0].rfind("/")
        if tsl < 0:
            urlpfx = dirpfx = m[0]
        else:
            urlpfx = m[0][:tsl] + "/"
            dirpfx = m[0][tsl + 1 :]
        urlsfx = re.match(r".+/([^/]+)", url[len(urlpfx) + 1 :])
        if urlsfx:
            urlsfx = urlsfx[1]
        else:
            urlsfx = ""

        if self.verbose:
            print(f"Fetching '{urlpfx}' for version expansion...")

        rx = re.compile(
            rf"""
            href=[\"']?
            ({re.escape(urlpfx)})?
            \.?/?
            ({re.escape(dirpfx)}[-_.0-9]*[0-9]({vdsfx})[\"'/])
        """,
            re.VERBOSE,
        )

        req = self._fetch(urlpfx)
        if not req:
            return ret

        reqs = list(set(map(lambda v: v[1], re.findall(rx, req))))
        if len(reqs) == 0:
            return ret

        reqs.sort(key=lambda v: _ver_conv(v.rstrip("/")), reverse=True)

        for v in reqs:
            nurl = f"{urlpfx}{v}{urlsfx}"
            if nurl == url:
                break
            if self.verbose:
                print(f"Adding '{nurl}' for version check...")
            ret.append(nurl)

        return ret

    def fetch_versions(self, url):
        rx = None
        rxg = None
        pname = self.pkgname

        if not self.url:
            # TODO: cran, crates.io
            if "sourceforge.net/sourceforge" in url:
                pn = url.split("/")[4]
                url = f"https://sourceforge.net/projects/{pn}/rss?limit=200"
            elif "launchpad.net" in url:
                pn = url.split("/")[3]
                url = f"https://launchpad.net/{pn}/+download"
            elif "pythonhosted.org" in url:
                if pname == self.template.pkgname:
                    pname = pname.removeprefix("python-")
                url = f"https://pypi.org/simple/{pname}"
            elif "rubygems.org" in url:
                if pname == self.template.pkgname:
                    pname = pname.removeprefix("ruby-")
                url = f"https://rubygems.org/gems/{pname}"
                rx = rf"""
                    /gems/{re.escape(pname)}/versions/([\d.]+)(?=")
                """
            elif "cpan." in url:
                if pname == self.template.pkgname:
                    pname = pname.removeprefix("perl-")
            elif "github.com" in url:
                pn = "/".join(url.split("/")[3:5])
                url = f"https://github.com/{pn}/tags.atom"
                rx = rf"""
                    /releases/tag/
                    (v?|V?|{re.escape(pname)}-)?
                    ([\d.]+)(?=") # match
                """
                rxg = 1
            elif "//gitlab." in url or "salsa.debian.org" in url:
                pn = "/".join(url.split("/")[0:5])
                url = f"{pn}/-/tags?format=atom"
                rx = rf"""
                    {re.escape(pn)}/-/tags/
                    (v?|V?|{re.escape(pname)}-)?
                    ([\d.]+)(?=\") # match
                """
                rxg = 1
            elif "bitbucket.org" in url:
                pn = "/".join(url.split("/")[3:5])
                url = f"https://bitbucket.org/{pn}/info/refs?service=git-upload-pack"
                rx = rf"""
                    refs/tags/
                    (v?|V?|{re.escape(pname)}-)?
                    ([\d.]+)(?!^) # match
                """
                rxg = 1
            elif "ftp.gnome.org" in url or "download.gnome.org" in url:
                rx = rf"""
                    {re.escape(pname)}-
                    ((0|[13]\.[0-9]*[02468]|[4-9][0-9]+)\.[0-9.]*[0-9])(?=)
                """
                rxg = 0
                url = f"https://download.gnome.org/sources/{pname}/cache.json"
            elif "archive.xfce.org" in url:
                pn = "/".join(url.split("/")[4:6])
                url = f"https://gitlab.xfce.org/{pn}/-/tags?format=atom"
                rx = rf"""
                    {re.escape(pn)}/-/tags/
                    ({re.escape(pname)}-)?v? # lol
                    ([\d.]+)(?=\") # match
                """
                rxg = 1
            elif "kernel.org/pub/linux/kernel/" in url:
                mver = ".".join(self.pkgver.split(".")[0:2])
                rx = rf"{mver}[\d.]+(?=\.tar\.xz)"
            elif "codeberg.org" in url:
                pn = "/".join(url.split("/")[3:5])
                url = f"https://codeberg.org/{pn}/tags"
                rx = rf"""
                    /archive/
                    (v?|V?|{re.escape(pname)}-)?
                    ([\d.]+)(?=\.tar\.gz) # match
                """
                rxg = 1
            elif "hg.sr.ht" in url:
                pn = "/".join(url.split("/")[3:5])
                url = f"https://hg.sr.ht/{pn}/tags"
                rx = rf"""
                    /archive/
                    (v?|{re.escape(pname)}-)?
                    ([\d.]+)(?=\.tar\.gz") # match
                """
                rxg = 1
            elif "git.sr.ht" in url:
                pn = "/".join(url.split("/")[3:5])
                url = f"https://git.sr.ht/{pn}/info/refs"
                rx = rf"""
                    refs/tags/
                    (v?|V?|{re.escape(pname)}-)?
                    ([\d.]+)(?!^) # match
                """
                rxg = 1
            elif "pkgs.fedoraproject.org" in url:
                url = f"https://pkgs.fedoraproject.org/repo/pkgs/{pname}"
            elif "pagure.io" in url:
                url = f"https://pagure.io/{pname}/releases"

        if self.pattern:
            rx = self.pattern
            rxg = None

        if self.group:
            rxg = self.group

        if not rx:
            rx = rf"""
                (?<!-)\b
                {re.escape(pname)}
                [-_]?
                ((src|source)[-_])?v?
                ([^-/_\s]*?\d[^-/_\s]*?) # match
                (?=
                    (?:
                        [-_.](?:src|source|orig)
                    )?\.(?:
                        [jt]ar|shar|t[bglx]z|tbz2|zip
                    )
                )\b
            """
            rxg = 2

        rx = re.compile(rx, re.VERBOSE)

        if self.verbose:
            print(f"Fetching '{url}' for version checks...")

        req = self._fetch(url)

        if not req:
            if req is False and self.verbose:
                print(f"Already fetched '{url}', skipping...")
            return []

        reqs = re.findall(rx, req)

        if rxg is not None:
            return list(map(lambda v: v[rxg].replace("_", "."), reqs))

        return list(map(lambda v: v.replace("_", "."), reqs))


def update_check(pkg, verbose=False, error=False):
    uc = UpdateCheck(pkg, verbose)

    tpath = pkg.template_path

    collect_sources = None
    expand_source = None
    fetch_versions = None
    checkvers = []

    if verbose:
        print(f"Checking for updates: {pkg.pkgname}={pkg.pkgver}")

    if (tpath / "update.py").exists():
        modspec = importlib.util.spec_from_file_location(
            pkg.pkgname + ".update", tpath / "update.py"
        )
        modh = importlib.util.module_from_spec(modspec)

        setattr(builtins, "self", uc)
        modspec.loader.exec_module(modh)
        delattr(builtins, "self")

        if verbose:
            print("Found update.py, using overrides...")

        # hooks

        if hasattr(modh, "collect_sources"):
            collect_sources = modh.collect_sources

        if hasattr(modh, "expand_source"):
            expand_source = modh.expand_source

        if hasattr(modh, "fetch_versions"):
            fetch_versions = modh.fetch_versions

        # variables

        if hasattr(modh, "pattern"):
            uc.pattern = modh.pattern

        if hasattr(modh, "group"):
            uc.group = modh.group

        if hasattr(modh, "url"):
            uc.url = modh.url

        if hasattr(modh, "pkgname"):
            uc.pkgname = modh.pkgname

        if hasattr(modh, "pkgver"):
            uc.pkgver = modh.pkgver

        if hasattr(modh, "single_directory"):
            uc.single_directory = modh.single_directory

        if hasattr(modh, "ignore"):
            uc.ignore = modh.ignore

        if hasattr(modh, "vdprefix"):
            uc.vdprefix = modh.vdprefix

        if hasattr(modh, "vdsuffix"):
            uc.vdsuffix = modh.vdsuffix

    if uc.ignore is True or pkg.build_style == "meta":
        return checkvers

    if uc.ignore and type(uc.ignore) is not list:
        if error:
            return None
        print(f"CAUTION: malformed ignore list for {pkg.pkgname}")
        return checkvers

    # use hooks if defined

    if collect_sources:
        ics = collect_sources(uc)
    else:
        ics = uc.collect_sources()

    cs = []
    for u in ics:
        if expand_source:
            cs += expand_source(uc, u)
        else:
            cs += uc.expand_source(u)

    retry_delays = [0, 2, 5, 10]
    vers = None

    for d in retry_delays:
        vers = []

        for src in cs:
            if fetch_versions:
                vers += fetch_versions(uc, src)
            else:
                vers += uc.fetch_versions(src)

        if len(vers) > 0:
            break

        time.sleep(d)

        if verbose:
            print("No versions fetched, retrying...")

    vers = list(set(vers))
    vers.sort(key=_ver_conv)

    if len(vers) == 0:
        if error:
            return None

        print(f"CAUTION: no version found for '{pkg.full_pkgname}'")

    for v in vers:
        if verbose:
            print(f"Checking found version: {v}")

        ignored = False

        for iv in uc.ignore:
            if fnmatch.fnmatchcase(v, iv):
                ignored = True
                if verbose:
                    print(f"Ignoring version '{v}' (due to '{iv}')")
                break

        if ignored:
            continue

        ret = apkcli.compare_version(
            uc.pkgver.replace("-", "."), v.replace("-", "."), False
        )
        if ret == -1:
            checkvers.append((pkg.pkgver, v))

    return checkvers


def check_pkg(pkg):
    cv = update_check(pkg, False, True)
    if cv is None:
        pkg.error("no versions found, broken update-check?")

    for pv, nv in cv:
        pkg.log_warn(f"update available: {pv} -> {nv}")

    if cv:
        pkg.error("updates found, aborting")
